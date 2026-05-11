import curses,time

def dashboard(stdscr):
    try:
        curses.curs_set(0)
        curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
        try:
            linha,coluna = stdscr.getmaxyx()
            mensagem = "Teste de terminal"
            logica = stdscr.addstr(linha//2,(coluna - len(mensagem))//2,mensagem,
                          curses.color_pair(1)|curses.A_BOLD)
            aviso = "Pressione qualquer tecla para sair"
            stdscr.addstr(linha -1,0,aviso,curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return False
    except Exception as f:
        print(f"Ocorreu um erro: {f}")
        return False
if __name__ == "__main__":
    curses.wrapper(dashboard)