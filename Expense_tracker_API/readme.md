Projeto envolvendo a montagem de uma API para gerenciamento de despesas, com uso de validaçao de dados **Pydantic**, criptofrafia de senhas com **bcrypt** e autenticação com **OAuth2 e JWT**.

O projeto adota arquitetura e modularização dividida responsavelmente para facilitar a manutenção, testabilidade e escalabilidade.

1. Api: Responsável por interceptar as requisições externas, direcionar os fluxos de execução e formatar as respostas entregues ao cliente.

2. Core: Centraliza funções globais e regras de negócio de infraestrutura de segurança.

3. Models: Garante a integridade absoluta de todas as informações que entram e residem no sistema.

4. Main: Sua única e crucial responsabilidade é instanciar o framework FastAPI, acoplar todas as tubulações dos roteadores de módulos de forma centralizada e coordenar a inicialização do servidor ASGI Uvicorn na rede local.


@derbitr