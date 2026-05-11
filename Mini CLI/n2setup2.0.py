import curses
import curses.panel
import time,traceback

def painel(stdscr):
    curses.curs_set(0)
    try:
        linhas,colunas = stdscr.getmaxyx()
        limite = min(5, linhas - 1)
        for i in range(limite):
            stdscr.addstr(i,0,"Fundo Painel")
        stdscr.refresh()
        time.sleep(1)
        curses.flushinp()
        altura_popup = 5
        largura_popup = 20
        if linhas <altura_popup or colunas < largura_popup:
            stdscr.clear()
            stdscr.addstr(0,0,"Terminal pequeno")
            stdscr.refresh()
            stdscr.getch()
            return None
        inicio_x = (linhas - altura_popup)//2
        inicio_y = (colunas - largura_popup)//2
        janela_popup = curses.newwin(altura_popup,largura_popup,inicio_x,inicio_y)
        painel_popup = curses.panel.new_panel(janela_popup)
        janela_popup.erase()
        janela_popup.box()
        text = "Pablo gordo" #Pablo é meu amigo e estava comigo enquanto eu codava :)
        meio_text = (largura_popup - len(text)) // 2
        if meio_text > 0:
            janela_popup.addstr(2,meio_text,text)
        else:
            janela_popup.addstr(1,2,"Text grande")
        janela_popup.refresh()
        janela_popup.getch()
    except Exception:
        return traceback.format_exc()
if __name__ == "__main__":
    resultado = curses.wrapper(painel)
    if resultado:
        print(f"Erro")
        print(resultado)