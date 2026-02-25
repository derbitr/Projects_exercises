from PIL import Image
from pathlib import Path

def processar_imagens(origem,destino):
    origem_str = Path(origem)
    destino_str = Path(destino)
    destino_str.mkdir(exist_ok=True)
    for i in Path(origem_str).iterdir():
        if i.is_file() and i.suffix.lower() in [".jpg",".png",".jpeg"]:
            a = Image.open(i)
            mudanca_cor = a.convert("L")
            mudanca_final = mudanca_cor.resize((20,20))
            guardar_arquivo = destino_str/i.name
            mudanca_final.save(guardar_arquivo)
            a.close()
if __name__ == "__main__":
    processar_imagens("e:/Downloads opera/twitter_media_harvest","e:/Usuário/Breno/Teste") #Pequeno teste que eu fiz usando uma biblioteca que eu baixo um monte de coisa via twitter usando uma extensao
                                                                                            #E jogando pra uma pasta de teste. Deu certo.
