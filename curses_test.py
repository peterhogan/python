from time import sleep
## Beginning ##
import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
## Beginning ##


for i in range(4):
    sleep(1)
    print("PISS!!!")











## Ending ##
curses.nocbreak()
stdscr.keypad(True)
curses.echo()
curses.endwin()
## Ending ##
