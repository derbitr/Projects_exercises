import pathlib as ptl
import shutil
pasta = ptl.Path("Meus arquivos")
pasta.mkdir(exist_ok = True)
try:
    with pasta.open("w", encoding="utf-8") as f:
        f.write("Pasta criada")
except FileNotFoundError:
    print("Arquivo nao encontrado")
mapping = {'.pdf': 'Documentos', '.jpg': 'Imagens'}
download = ptl.Path("e:\Downloads")
for map,down in mapping.items():
    destino_path = pasta / down
    destino_path.mkdir(exist_ok = True)
    for item in download.rglob(f"*{map}"):
        shutil.move(item, destino_path/item.name)
for sub in pasta.iterdir():
    print(sub)
    for arquivo in sub.iterdir():
        print("-",arquivo.name)