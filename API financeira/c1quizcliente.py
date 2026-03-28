import requests
import c3dados
def jogar():
    try:
        perguntas = c3dados.carregar_perguntas()
        progresso = c3dados.carregar_progresso()
        if not perguntas:
            return
        pergunta_atual = int(progresso["pergunta"])
        pontuacao = int(progresso["pontuacao"])
        while True:
            pergunta_chave = str(pergunta_atual)
            if pergunta_chave not in perguntas:
                print("Conectando a bola de premios")
                try:
                    resposta_api = requests.get(f"http://127.0.0.1:8003/premio/{pontuacao}")
                    resposta_api.raise_for_status()
                    dados_premio = resposta_api.json()
                    print({
                            "Pontos" : dados_premio["Pontos"],
                            "Prêmio em dólar": dados_premio["Prêmio em dólar"],
                            "Cotaçao usada": dados_premio["Cotação usada"],
                            "Prêmio em real" : dados_premio["Prêmio em real"],
                            "Link para compartilhar":dados_premio["Link para compartilhar"]
                        })                        
                except Exception as g:
                    print(f"Ocorreu um erro: {g}")
                estado_zerado = {
                    "pergunta" : "1", "pontuacao" : 0
                }
                c3dados.salvar_progresso(estado_zerado)
                break
            else:
                dados_pergunta = perguntas[pergunta_chave]
                print(dados_pergunta["pergunta"])
                for opcao in dados_pergunta["opcoes"]:
                    print(opcao)
                resposta = input("Sua resposta (A, B, C) ou 'S' para sair ou salvar:").upper()
                if resposta == "S":
                    print("Saindo e salvando")
                    break
                elif resposta == dados_pergunta["resposta_correta"]:
                    print("Acertou")
                    pontuacao += 10
                else:
                    print("Errou")
                    print(dados_pergunta["resposta_correta"])
                pergunta_atual += 1
                novo_estado = {
                    "pergunta": str(pergunta_atual),
                    "pontuacao": pontuacao
                }
                c3dados.salvar_progresso(novo_estado)
    except Exception as e:
        print(f"Ocorreu um erro ao inicializar o quiz: {e}")
        return
if __name__ == "__main__":
    jogar()
