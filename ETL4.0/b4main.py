import b1banco,b2modelos,b3extraçao,logging

def iniciar():
    b1banco.config_log()
    logging.info("Iniciando sistema de registros")
    b1banco.criar_tabela()
    logging.info("Tabela criada")
    try:
        validar_dados = b3extraçao.capturar_dados()
        if validar_dados:
            b1banco.inserir_dados(validar_dados)
            filtro = b1banco.contar_ano(2)
            if filtro:
                logging.info(f"Enviando {len(filtro)}")
                b1banco.enviar_nuvem(filtro)
            else:
                logging.warning("Nenhum dado")
        logging.info("Finalizado")
    except Exception as e:
        logging.error(F"Erro ao validar dados")
        return False
if __name__ == "__main__":
    iniciar()
