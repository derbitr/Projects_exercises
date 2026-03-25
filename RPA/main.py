import c2banco,c3excel
import c1sentinela
def iniciar_banco():
    c2banco.tabela()
def menu():
    print("Sistema de escolhas")
    print("[1] Ligar observador\n[2] Gerar relatório Excel\n[3] Sair")
    while True:
        escolha = input("Escolha as opções abaixo digitando 1,2 ou 3 no console: ")
        if escolha == "1":
            c1sentinela.sentinela()
            print("Observador criado")
        elif escolha == "2":
            c3excel.relatorio()
            print("Excel criado")
        elif escolha == "3":
            break
        else:
            print("Opção inválida")
if __name__ == "__main__":
    iniciar_banco()
    menu()