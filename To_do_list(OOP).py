import json
from collections import defaultdict,UserDict,deque,OrderedDict
import os
import time
class Tarefa:
    def __init__(self,titulo : str,concluido : bool = False):
        self.titulo = titulo
        self.concluido = concluido
    def marcar_conclusao(self):
        if not self.concluido:
            self.concluido = True
            print(f" a tarefa {self.titulo} foi concluída")
        else:
            print(f" a tarefa {self.titulo} já está concluída")
    def dicionario_json(self):
        return {
            "Título" : self.titulo,
            "Status de conclusao" : self.concluido
        }
class Listadetarefas():
    def __init__(self):
        self.caixa = []
    def adicionar_tarefa(self,titulo):
        novo_titulo = Tarefa(titulo)
        self.caixa.append(novo_titulo)
    def listar_tarefas(self):
        if not self.caixa:
            print("lista vazia")
            return
        for i, tarefa in enumerate(self.caixa,start=1):
            print(f" {i}, {tarefa.titulo}")
    def remover_tarefa(self,indice : int):
            if 0<= indice - 1 < len(self.caixa):
                remover_tarefa = self.caixa.pop(indice-1)
                print(f"{remover_tarefa.titulo}")
                return        
            print(f"Tarefa nao encontrada")
    def concluir_tarefa(self,indice: int):
        if 0<= indice - 1 < len(self.caixa):
            tarefa_alvo = self.caixa[indice-1]
            tarefa_alvo.marcar_conclusao()
        else:
            print("Tarefa nao encontrada")
    def salvar_dados(self, nome_arquivo="ficheiro.json"):
        try:
            dados = [tarefa.dicionario_json() for tarefa in self.caixa]
            with open(nome_arquivo, "w", encoding= "utf-8") as f:
                json.dump(dados ,f,ensure_ascii=False,indent=4)
            print("Dados salvos")
        except(OSError,IOError) as e:
            print(f"Erro ao salvar o arquivo: {e}")
    def carregar_dados(self,nome_arquivo = "ficheiro.json"):
        if not os.path.exists(nome_arquivo):
            print("Não encontrado")
            return None
        try:
            with open(nome_arquivo, "r",encoding="utf-8") as f:
                dados_carregados = json.load(f)
                for item in dados_carregados:
                    tarefa_recuperada = Tarefa(item["Título"],item["Status de conclusao"])
                    self.caixa.append(tarefa_recuperada)
        except(OSError,IOError) as g:
            print(f"Erro encontrado: {g}")
            return None
if __name__ == "__main__":
    t1 = Listadetarefas()
    t1.carregar_dados()
    while True:
        menu = input("Lista de comandos\n 1 : Ver tarefas\n 2 : Adicionar tarefas\n 3 : Concluir tarefa\n 4 : Remover tarefa\n 5 : Sair")
        if menu == "1":
            t1.listar_tarefas()
        elif menu == "2":
            titulo = input("Digite a tarefa")
            t1.adicionar_tarefa(titulo)
            print("Processando..")
            time.sleep(3.0)
            print("Tarefa adicionada!")
        elif menu == "3":
            t1.listar_tarefas()
            try:           
                tconcluir = int(input("Qual tarefa está concluida"))
                t1.concluir_tarefa(tconcluir)
            except ValueError:
                print("Valor invalido")
        elif menu == "4":
            t1.listar_tarefas()
            try:
                tremover = int(input("Qual tarefa quer remover?"))
                t1.remover_tarefa(tremover)
            except ValueError:
                print("Valor invalido,tente novamente")
        elif menu == "5":        
            print("Salvando dados antes de sair..")
            time.sleep(2.0)
            t1.salvar_dados()
            print("Dados salvos!")
            break
