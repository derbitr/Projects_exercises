from PIL import Image,ImageDraw; import logging; import time

def relatorio(cidade : str, temp : float, desc : str,imagem_inicial : str= "alan.jpg") -> str:
    if not cidade or not cidade.strip():
        logging.error("Nome de cidade invalido ou não existe")
        return None
    try:
        with Image.open(imagem_inicial) as img:
            logging.info("Procurando imagem...")
            desenhar = ImageDraw.Draw(img)
            logging.info("Alterando imagem..")
            texto_clima = f"Previsao para {cidade}:\nTemperatura : {temp}\nGraus,desc : {desc}"
            desenhar.text((40,40),texto_clima,fill="black")
            saida = f"relatorio_{cidade}.jpg"
            img.save(saida)
        return saida
    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado")
        return None
    except Exception as e:
        logging.error(f"Falha ao carregar o arquivo : {e}")
        return None
