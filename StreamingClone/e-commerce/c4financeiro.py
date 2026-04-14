
import stripe,c3estoque,os
from fastapi import FastAPI, Request, HTTPException,APIRouter
stripe.api_key="sk_teste_CHAVE_SECRETA" #Teste, não coloquei chaves reais
final = "whsec_Meu_FINAL_SECRET" #Também

roteador = APIRouter(prefix="/pagamentos", tags=["Financeiro"])

def criar_sessao(id_pedido : int, valor_total = float):
    sessao = stripe.checkout.Session.create(
        metadata={"pedido_id":id_pedido},
        payment_method_types=['card'],
        line_items= [{
            'price_data': {
                'currency': 'brl',
                'product_data': {
                    'name': id_pedido,
                    'description': 'Camisa confortável',
                    'images': ['https://example.com/Camisa'],
                },
                'unit_amount': int(valor_total*100),
            },
            'quantity':1,
        }],
        mode='payment',
        success_url=f'https://example.com/sucess?session_id={id_pedido}',
        cancel_url='https://example.com/cancel',
    )

@roteador.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        evento = stripe.Webhook.construct_event(
            payload,sig_header,final
        )
    except ValueError:
        raise HTTPException(status_code=400,detail="inválido")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400,detail="Assinatura inválida")
    if evento["type"] == "checkout.session.completed":
        id_pedido = int(evento["data"]["object"]["metadata"]["pedido_id"])
        if id_pedido:
            db = next(c3estoque.banco_local())
            try:
                c3estoque.confirmar_venda(id_pedido,db=db)
                db.commit()
            except Exception as f:
                db.rollback()
                raise HTTPException(status_code=500,detail=f"Erro no banco: {f}")
            finally:
                db.close()
        else:
            return
    return {"status": "success"}
    