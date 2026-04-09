from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, FastAPI, HTTPException, Depends
import v1banco,v2modelos,v3moldes,v4jwt,os,dotenv
from groq import Groq

dotenv.load_dotenv()

def banco_local():
    banco = v1banco.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
async def verificar_dados(usuario_interno : v2modelos.Usuario, db:Session):
    tarefas_query = db.query(v2modelos.Tarefa).filter(v2modelos.Tarefa.dono_id==usuario_interno.id).all()
    try:
        if len(tarefas_query) == 0:
            titulos_nas_tarefas_final = "Sem tarefas pendentes"
        else:
            texto_tarefas = "Tarefas Disponíveis"
            titulos_na_tarefa = []
            for elemento in tarefas_query:
                titulos_na_tarefa.append(elemento.titulo)
            titulos_nas_tarefas_final = ",".join(titulos_na_tarefa)
        return titulos_nas_tarefas_final
    except Exception as e:
        return f"Ocorreu um erro: {e}"
async def dados(usuario_interno: v2modelos.Usuario, db: Session):
    try:
        memoria_query = db.query(v2modelos.MensagemChatBot).filter(v2modelos.MensagemChatBot.dono_id == usuario_interno.id).order_by(v2modelos.MensagemChatBot.id.desc()).limit(5).all()
        inverter_memoria = memoria_query[::-1]
        return inverter_memoria
    except Exception as f:
        return f"Não foi possível acessar o banco de dados: {f}"
async def traducao_bot_ia(usuario_interno:v2modelos.Usuario,pergunta : v3moldes.ChatEntrada,db : Session):
    try:
        cliente = Groq(
            api_key= os.environ.get("API_KEY")
        )
        tarefas = await verificar_dados(usuario_interno,db)

        historico = await dados(usuario_interno, db)

        lista_tarefas_groq = []

        prompt_sistema = {
            "role" : "system",
            "content" : f"Você é um assistente pessoal. O usuario {usuario_interno.username} vai enviar perguntas generalistas ou específicas e você vai analisar e responder adequadamente, seu objetivo é explicar cada pedido do usuário. As tarefas listadas: {tarefas}"
        }
        lista_tarefas_groq.append(prompt_sistema)
        for item in historico:
            lista_tarefas_groq.append({"role": item.papel, "content": item.conteudo})
        lista_tarefas_groq.append({"role" : "user", "content" : pergunta.mensagem})
        resposta_bot = cliente.chat.completions.create(model ="moonshotai/kimi-k2-instruct-0905",
                                                       messages = lista_tarefas_groq,
                                                       max_tokens=100,
                                                       temperature=0.9)
        lista_tarefas_groq.append({
            "role":"assistant",
            "content": resposta_bot.choices[0].message.content
        })
        print(F"Assistant : {resposta_bot.choices[0].message.content}")
        usuario = v2modelos.MensagemChatBot(
            papel = "user",
            conteudo = pergunta.mensagem,
            dono_id = usuario_interno.id
        )
        IA = v2modelos.MensagemChatBot(
            papel = "assistant",
            conteudo = resposta_bot.choices[0].message.content,
            dono_id = usuario_interno.id
        )
        db.add(usuario)
        db.add(IA)
        db.commit()
        return {"resposta": resposta_bot.choices[0].message.content}
    except Exception as g:
        return f"Erro ao processar : {g}"