import random
import curses
import time
from curses import wrapper

# sc = curses.initscr()


def main(stdscr):
    h, w = stdscr.getmaxyx()
    win = curses.newwin(h, w, 0, 0)

    # curses.curs_set(0)
    curses.cbreak()
    win.keypad(True)
    # curses.echo(True)
    stdscr.refresh()
    for i in range(24):
        win.addstr("hello, my name is kelsey"[i])
        time.sleep(.1)
        win.refresh()
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break  # Exit the while loop
        elif c == ord('p'):
            win.addch(5, 10, curses.ACS_DIAMOND)
            win.refresh()

wrapper(main)
