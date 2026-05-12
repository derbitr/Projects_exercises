import argparse,traceback
import time


def iniciar():
    parser = argparse.ArgumentParser(description="Ferramenta de teste" )
    try:
        grupo_log = parser.add_mutually_exclusive_group()
        grupo_log.add_argument("-v","--verbose",action="store_true",help="Mostra todos os logs")
        grupo_log.add_argument("-q","--quiet",action="store_true",help="Oculta todos os logs")
        try:
            subparses = parser.add_subparsers(dest="comando",help="Comandos disponíveis")
            parser_banco = subparses.add_parser("banco",help="Gerencia banco de dados")
            parser_banco.add_argument("--acao",choices=["iniciar","deletar"],required=True,help="O que fazer com o banco")
            try:
                parser_importar = subparses.add_parser("importar",help="Importa itens para o banco")
                parser_importar.add_argument("arquivo",type=argparse.FileType("r"),help="Caminho para o comando ler o arquivo")
            except Exception:
                return traceback.format_exc()
        except Exception:
            return traceback.format_exc()
    except Exception:
        return traceback.format_exc()
    try:
        args = parser.parse_args()
        if args.verbose:
            print(f"[LOG] iniciando execução")
        if args.comando == "banco":
            print(f"Executando ação '{args.acao} no banco de dados")
        elif args.comando == "importar":
            conteudo = args.arquivo.read()
            print(f"Importando o arquivo...")
            time.sleep(0.5)
            print(f"Dados: {conteudo:20}")
        else:
            parser.print_help()
    except Exception:
        return traceback.format_exc()
if __name__ == "__main__":
    iniciar()