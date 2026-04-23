import stripe, x1redis,x2modelos,x3motor,x4rotas,os
from fastapi import FastAPI, Request, HTTPException,APIRouter,Depends
from dotenv import load_dotenv
load_dotenv()

stripe.api_key = os.getenv("STRIPE_API_KEY")

def processar(payload : dict):
    conteudo = stripe.PaymentIntent.create(
        amount = payload['valor'],
        currency= payload['moeda'],
        payment_method=payload['metodo_id'],
        confirm=True,
        off_session=True,
        automatic_payment_methods={"enabled":True,"allow_redirects":"never"},
        idempotency_key=payload["task_id"]
    )
    return conteudo