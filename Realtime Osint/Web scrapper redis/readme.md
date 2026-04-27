Projeto de um scrapper bot usando um novo conceito de otimização de memória (Redis) com lógica, arquitetura limpa e modularização.

v1redis: Configura a comunicação entre a API e os Workers usando o Redis como mensageiro.

v2modelos: Define modelos Pydantic para garantir que os dados de entrada e saída são válidos e seguem um contrato rigoroso.

v3worker: Recebe as tarefas da fila, gere o ciclo de vida da execução e lida com retentativas (Retry) automáticas.

v4rotas: Interface FastAPI que recebe pedidos do utilizador e os despacha para processamento em background.

v5logica: Contém a lógica pura de raspagem usando HTTPX para rede e BeautifulSoup para extração de HTML.

v6main: Contem a configuração para rodar os principais arquivos do projeto