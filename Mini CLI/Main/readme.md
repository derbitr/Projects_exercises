Cli própria criada para aprendizado de conceitos de testes de extração de dados com interface interativa via terminal (vscode,bash,cmd).

Guia:

**Bash**
**1** Opçoes disponiveis no menu:
1 = Executa ação
2 = Importa arquivo (Pede o nome do arquivo)
3 = Teste da interface
0 = Sai da cli

**2** Direto no terminal
python main.py -v banco --acao iniciar

**3** Deletar banco
python main.py -v banco --acao deletar

**4** Testar importação de arquivo
python main.py importar *nome_do_arquivo.txt*

**Clone ou baixe o repositório**

**Dependencias necessárias!**
'''bash
pip install -r requirements.txt