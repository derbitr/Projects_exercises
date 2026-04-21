Sistema modular de alta performance para venda e distribuição de conteúdo em vídeo.

x1 / x2 (Dados): Configuração do Postgres e Modelos (Usuários, Cursos, Pedidos).

x3 (Mídia): Motor de streaming binário fragmentado (O(1) RAM) com suporte a Range Requests.

x4 / x5 (Vendas): Integração Stripe (Checkout/Webhook) com Lock Pessimista para controle de vagas.

x6main.py: Orquestrador central e inicialização de tabelas.  