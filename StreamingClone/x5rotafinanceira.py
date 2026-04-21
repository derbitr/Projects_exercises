import stripe,x3motor,x3motorrotas,x1banco,x4estoque
from fastapi import FastAPI, Request, HTTPException,APIRouter
stripe.api_key = "sk_teste_secreto" #Teste, não é chave real
final = "whsec_Meu_FINAL_SECRET" #tambem

roteador = APIRouter(prefix="/pagamentos",tags=["Financeiro"])

def criar_sessao(id_pedido : int, valor_total : float, caminho_video: str):
    try:
        sessao = stripe.checkout.Session.create(
            metadata={"pedido_id":str(id_pedido)},
            payment_method_types=['pix','card'],
            line_items=[{
                'price_data':{
                    'currency': 'brl',
                    'product_data': {
                        'name': id_pedido,
                        'description': 'Video fofo'

                    },
                    'unit_amount': int(valor_total*100),
                },
                'quantity':1,
            }],
            mode='payment',
            success_url=f"htpps://example.com/sucess?session_id={id_pedido}",
            cancel_url="htpps://example.com/cancel"
        )
        return sessao
    except Exception as g:
        raise HTTPException(status_code=500,detail=str(g))
    
@roteador.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    try:
        evento = stripe.Webhook.construct_event(
            payload, sig_header,final

        )
    except ValueError:
        raise HTTPException(status_code=400,detail="Inválido")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400,detail="Assinatura inválida")
    if evento["type"] == "checkout.session.completed":
        id_pedido = int(evento["data"]["object"]["metadata"]["pedido_id"])
        if id_pedido:
            db = next(x1banco.get_db())
            try:
                x4estoque.transações(id_pedido,db=db)
                db.commit()
            except Exception as f:
                db.rollback()
                raise HTTPException(status_code=500,detail=f"Erro no banco: {f}")         
            finally:
                db.close()
        else:
            return
    return {"status": "success"}      

