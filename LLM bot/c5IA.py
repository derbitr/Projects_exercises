from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter,FastAPI,HTTPException,Depends
import c1banco,c2modelos,c3moldes,c4jwt,os,dotenv
from groq import Groq

dotenv.load_dotenv()


def banco_local():
    banco = c1banco.Sessao_local()
    try:
        yield banco
    finally:
        banco.close()
async def verificar_dados(usuario_interno :c2modelos.Usuario ,db: Session = Depends(banco_local)):
    tarefas_query = db.query(c2modelos.Tarefa).filter(c2modelos.Tarefa.dono_id == usuario_interno.id).all()
    try:
        if len(tarefas_query) == 0:
            titulos_nas_tarefas_final = "Sem tarefas pendentes"
        else:
            texto = "Tarefas disponíveis"
            titulos_na_tarefa = []
            for elemento in tarefas_query:
                titulos_na_tarefa.append(elemento.titulo)
            titulos_nas_tarefas_final = ",".join(titulos_na_tarefa)
        return titulos_nas_tarefas_final
    except Exception as e:
        return f"Ocorreu um erro: {e}"
async def memoria_dados(usuario_interno : c2modelos.Usuario,db : Session = Depends(banco_local)):
    try:
        memoria_query = db.query(c2modelos.MensagemChat).filter(c2modelos.MensagemChat.usuario_id == usuario_interno.id).order_by(c2modelos.MensagemChat.id.desc()).limit(5).all()
        inverter_memoria = memoria_query[::-1]
        return inverter_memoria
    except Exception as g:
        return f"Não foi possível acessar o banco de dados: {g}" 
async def traducao_bot(usuario_interno :c2modelos.Usuario,pergunta : c3moldes.MensagemResposta ,db: Session = Depends(banco_local)):
    try:
        cliente = Groq(
            api_key=os.environ.get("API_KEY") # Mudar pq eu só pus para não dar erro no codigo(TA MUITO ERRADO)
        )
        string_tarefas = await verificar_dados(usuario_interno,db)

        historico_mensagens = await memoria_dados(usuario_interno,db)

        lista_tarefas_groq = []
    
        prompt_sistema = {
            "role" : "system",
            "content": f"você é um assistente pessoal. O usuario {usuario_interno.username} vai enviar perguntas generalistas ou específicas como 'tarefas', seu objetivo é explicar de maneira clara cada pedido do usuário. As tarefas listadas: {string_tarefas}"  
        }
        lista_tarefas_groq.append(prompt_sistema)
        for item in historico_mensagens:
            lista_tarefas_groq.append({"role": item.papel, "content": item.conteudo})
        lista_tarefas_groq.append({"role": "user", "content": pergunta.mensagem})
        resposta = cliente.chat.completions.create(model="moonshotai/kimi-k2-instruct-0905",
                                                        messages=lista_tarefas_groq,
                                                        max_tokens=100,
                                                        temperature=1.0)
        lista_tarefas_groq.append({
                "role": "assistant",
                "content": resposta.choices[0].message.content
            })
        print(f"Assistant: {resposta.choices[0].message.content}")
        usuario =  c2modelos.MensagemChat(
            papel = "user",
            conteudo = pergunta.mensagem,
            usuario_id = usuario_interno.id
        )
        IA = c2modelos.MensagemChat(
            papel = "assistant",
            conteudo = resposta.choices[0].message.content,
            usuario_id = usuario_interno.id
        )
        db.add(usuario)
        db.add(IA)
        db.commit()
        return {"resposta": resposta.choices[0].message.content}
    except Exception as h:
        return f"Erro ao processar: {h}"
