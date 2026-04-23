import stripe,x1redis,x2modelos,x3motor, requests,os
from fastapi import FastAPI, Request, HTTPException, APIRouter,Depends
from dotenv import load_dotenv
load_dotenv()

roteador = APIRouter(prefix="/Tarefas",tags=["Lista"])

@roteador.post("/Pagamento",response_model= x2modelos.Taskmodel)
async def  pagamentos(request : x2modelos.TaskRequest, banco = Depends(x1redis.get_redis())): #p = tarefa from x3motor
    nova_tarefa = x2modelos.Taskmodel(task_type=request.task_type,payload=request.payload)
    try:
        info = banco.hset("status_tarefa",str(nova_tarefa.id),nova_tarefa.status.value)
        if not info:
            return 0
        else:
            info_atualizada = banco.lpush("minha_fila",nova_tarefa.to_json())
            return nova_tarefa
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
@roteador.get("/status/{task_id}")
async def consulta(task_id :str , banco = Depends(x1redis.get_redis())):
    try:
        status = banco.hget("status_tarefa",str(task_id))
        if status:
            return status
        else:
            raise HTTPException(status_code=404,detail="Não encontrado")
    except Exception as f:
        raise HTTPException(status_code=500,detail=str(f))
@roteador.post("/webhook")
async def stripe_webhook(request:Request, banco = Depends(x1redis.get_redis())):
    payload = await request.body()
    sig_header = request.headers.get("stripe_signature")
    try:
        evento = stripe.Webhook.construct_event(
            payload,sig_header,secret=os.getenv("SEGREDO_TESTE")
        )
    except ValueError:
        raise HTTPException(status_code=400,detail="Inválido")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400,detail="Assinatura inválida")
    if evento["type"] == "checkout.session.completed":
        id_task = evento["data"]["object"]["metadata"].get("task_id")
        if id_task:
            banco.hset("status_tarefa",id_task,"Completado")
    return {"status": "success"}