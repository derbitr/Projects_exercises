from fastapi import FastAPI
from pydantic import BaseModel
import c2crud,uvicorn

class DespesaModel(BaseModel):
    titulo : str
    valor : float
    categoria : str
    data : str
app = FastAPI(title = "Rastreador de despesas")
@app.post("/items/")
def criar_despesa(despesa : DespesaModel):
    c2crud.despesas(despesa.titulo,despesa.valor,despesa.categoria,despesa.data)
    return {"Mensagem": "Dados da despesa salvos no banco de dados"}
@app.get("/items/")
def ler_despesas(dias:int):
    resultados = c2crud.filtrar_despesas(dias)
    return {"Conteúdo": resultados}
if __name__ == "__main__":
    print("Iniciando sistema...")
    uvicorn.run(app,host="127.0.0.1",port = 8001)
