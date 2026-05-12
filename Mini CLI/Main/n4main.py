import curses,time,curses.panel,traceback,argparse,sys

def dashboard(stdscr,mensagem):
    try:
        try:
            linha,coluna = stdscr.getxymax()
            altura_popup = 5
            largura_popup = max(20,len(mensagem) + 6)
            if linha < altura_popup or coluna < largura_popup:
                return
            inicio_x = (linha - largura_popup) // 2
            inicio_y = (coluna - altura_popup) // 2

            janela_popup = curses.newwin(altura_popup,largura_popup,inicio_x,inicio_y)
            curses.panel.new_panel(janela_popup)
            janela_popup.erase()
            janela_popup.box()
            meio_text = (largura_popup - len(mensagem)) // 2
            if meio_text >0:
                janela_popup.addstr(2,meio_text,mensagem)
            else:
                janela_popup.addstr(1,2,"Texto fora do esquadro")
            janela_popup.refresh()
            curses.flushinp()
            janela_popup.getch()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    except Exception:
        return traceback.format_exc()
def interface(stdscr):
    try:
        curses.curs_set(0)
        curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
        while True:
            stdscr.clear()
            linha,coluna = stdscr.getmaxyx()
            titulo = "Menu interativo"
            stdscr.addstr(1, (coluna - len(titulo))//2,titulo,curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(2,0,"_" * coluna)
            stdscr.addstr(4,5, "1 -> Executa ação")
            stdscr.addstr(5,5, "2 -> Importa o arquivo")
            stdscr.addstr(6,5, "3 -> Teste interface")
            stdscr.addstr(8,5, "0 -> Sair")
            stdscr.addstr(10,5, "Pressione a tecla desejada:")

            tecla = stdscr.getch()

            if tecla == ord("1"):
                stdscr.addstr(12,5,"Executando ação..")
                stdscr.refresh()
                time.sleep(1)
                dashboard(stdscr, "Acao 'iniciar' iniciada")
            elif tecla == ord("2"):
                stdscr.addstr(12,5, "Digite o nome do arquivo")
                stdscr.refresh()
                curses.echo()
                curses.curs_set(1)
                arquiv_bytes = stdscr.getstr(12,32,30)
                nome_arquivo = arquiv_bytes.decode("utf-8").strip()
                curses.noecho()
                curses.curs_set(0)
                if nome_arquivo:
                    try:
                        with open(nome_arquivo,"r",encoding="utf-8") as arquivo_aberto:
                            conteudo = arquivo_aberto.read()
                        dashboard(stdscr, f"Arquivo '{nome_arquivo}' lido")
                    except FileNotFoundError:
                        dashboard(stdscr, f"Arquivo '{nome_arquivo}' não encontrado")
                    except Exception as e:
                        dashboard(stdscr, f"Erro genérico: {e}")
            elif tecla == ord("3"):
                dashboard(stdscr, "Teste de interface")
            elif tecla == ord("0"):
                dashboard(stdscr, "Saindo..")
                break
    except Exception:
        return traceback.format_exc()
def iniciar_argparse():
    parser = argparse.ArgumentParser(description="Ferramenta de teste")
    try:
        grupo_Log = parser.add_mutually_exclusive_group()
        grupo_Log.add_argument("-v","--verbose",action="store_true",help="Mostra todos os logs")
        grupo_Log.add_argument("-q","--quiet",action ="store_true",help="Oculta todos os logs")
        try:
            subparser = parser.add_subparsers(dest="comando",help="Comandos disponíveis")
            parser_banco = subparser.add_parser("banco",help="Gerencia banco de dados")
            parser.add_argument("--acao",choices=["iniciar","deletar"],required=True,help="Comandos de ação")
            try:
                parser_importar = subparser.add_parser("importar",help="Importa itens selecionados")
                parser_importar.add_argument("arquivo",type=argparse.FileType("r"),help="Caminho para leitura de arquivo")
            except Exception:
                return traceback.format_exc()
        except Exception:
            return traceback.format_exc()
    except Exception:
        return traceback.format_exc()
    try:
        args = parser.parse_args()
        if args.verbose:
            print(f"[LOG] Iniciando execução...")
        if args.comando == "banco":
            print(f"Executando ação '{args.acao}..")
        elif args.comando == "importar":
            conteudo = args.arquivo.read()
            print(F"Importando arquivo")
            time.sleep(0.5)
            print(f"Dados: {conteudo:20}")
        else:
            parser.print_help()
    except Exception:
        return traceback.format_exc()
if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            iniciar_argparse()
        else:
            curses.wrapper(interface)
    except Exception as e:
        print(f"Erro: {e}")
        print(traceback.format_exc())