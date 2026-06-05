import os, dotenv

dotenv.load_dotenv()


chave_secreta = os.getenv("CHAVE_SECRETA")
algoritmo = os.getenv("ALGORITMO")
acessso_token = os.getenv("ACESSO_TOKEN_EXPIRACAO")

