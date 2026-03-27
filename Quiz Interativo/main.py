import c1dados,logging,c1dados

def iniciar():
    try:
        perguntas = c1dados.carregar_perguntas()
        respostas = c1dados.carregar_progresso()
        if not perguntas:
            logging.warning("Nenhuma pergunta encontrada")
            return
        pergunta_atual = int(respostas["pergunta_atual"])
        pontuacao = int(respostas["pontuacao"])
        while True:
            chave_pergunta = str(pergunta_atual)
            if chave_pergunta not in perguntas:
                print("Quiz terminado")
                break
            else:
                dados_pergunta = perguntas[chave_pergunta]
                print(dados_pergunta["pergunta"])
                for opcao in dados_pergunta["opcoes"]:
                    print(opcao)
                resposta = input("Sua resposta ( A, B , C ) ou 'S' para sair e salvar: ").upper()
                if resposta == "S":
                    print("Salvando e saindo")
                    break
                elif resposta == dados_pergunta["resposta_correta"]:
                    print("Acertou")
                    pontuacao += 10
                else:
                    print("Errou")
                    print(dados_pergunta["resposta_correta"])
                pergunta_atual += 1
                novo_estado = {
                            "pergunta_atual": str(pergunta_atual),
                            "pontuacao": pontuacao
                        }
                c1dados.salvar_progresso(novo_estado)
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
        return
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,format = "%(levelname)s : %(message)s")
    iniciar()

