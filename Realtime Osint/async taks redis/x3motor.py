import x1redis,x2modelos,x4rotas,x5services, logging


NOME_STATUS = "status_tarefa"
def setup():
    try:
        mapeamento = {"email": " "} #Need put the x5file function here.
        banco = x1redis.get_redis()
        while True:
            lista = banco.brpop("minha_fila",timeout=0)
            if not lista:
                logging.info("Lista vazia")
                return None
            else:
                string = lista[1]
                tarefa = x2modelos.Taskmodel.from_json(string)
                atualizar_processar = banco.hset(NOME_STATUS,str(tarefa.id),"Processando")
                try:
                    acao = mapeamento.get(tarefa.task_type)
                    if acao is not None:
                        acao(tarefa.payload)
                        atualizar_completo = banco.hset(NOME_STATUS,str(tarefa.id),"Completado")
                    else:
                        logging.warning("Está vazia")
                        atualizar_falha = banco.hset(NOME_STATUS,str(tarefa.id),"Falha")
                except Exception as e:
                    atualizar_falha = banco.hset(NOME_STATUS,str(tarefa.id),"Falha")
                    logging.error(f"Status falha atualizado: {e}")
    except Exception as f:
        logging.error(f"Falha ao iniciar dados: {f}")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format="%(levelname)s : %(message)s")
    setup()