Criei um robo de automação automático (RPA) orientado a eventos para estudos pessoais sobre conceitos utilizando análise de dados, extração com pandas e leituras de logs utilizando a biblioteca watchdog. Utilizei arquitetura limpa, modularização e dividi os arquivos para testar singularmente.


v1banco: Salva os dados e espelha para uma API (url falsa, apenas para estudos)

v2modelos: Pydantic para validação de dados

v3processadorpandas: Filtra e limpa as respectivas colunas

v4watchdog: Monitora as pastas selecionadas

v5exportadorexcel: Transforma os dados extraídos em um novo arquivo excel (.xlsx)