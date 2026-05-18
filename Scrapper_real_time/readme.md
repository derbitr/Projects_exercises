**Scrapper assíncrono em tempo real**

Sistema simples que faz web scraping em background sem travamento de telas, retorna o resultado via WebSocket, onde possui um front-end básico para inserção de URL, sistema de registros singulares, arquitetura limpa e aplicação de contêineres (docker) para execução em diversos sistemas.

**Tecnologias**

*FastAPI*: Gerencia o websockets e recebe as informações vindas do webscraping
*Celery*: Sistema de processamento em background
*Redis*: Banco de memória para gerenciamento de fila
*HTTPS + BeautifulSoup*: Ferramentas de extração de dados
*Docker + Docker Compose*: Infraestrutura de contêineres

**Como executar**

*1.* Clone este repositório

*2.* Tenha Docker desktop instalado e rodando

*3.* Abra o terminal na pasta principal do projeto e execute este comando: "docker-compose up --build"

*4.* Abra o "index.html" no navegador e comece a busca