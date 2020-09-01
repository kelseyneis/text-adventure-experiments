import random
import curses
import time
from curses import wrapper


class GameWindow():
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.refresh()
        self.height, self.width = self.screen.getmaxyx()  # 40, 111
        self.win = curses.newwin(self.height, self.width, 0, 0)
        self.win.refresh()
        curses.curs_set(2)
        curses.cbreak()
        self.win.keypad(True)
        self.win.scrollok(True)
        # # curses.echo(True)

    def play(self):
        try:
            for i in range(50):
                self.add_text("hello, my name is kelsey. I'm from Minnesota hello, my name is kelsey. I'm from Minnesota hello, my name is kelsey. I'm from Minnesota hello, my name is kelsey. I'm from Minnesota hello, my name is kelsey. I'm from Minnesota")
                curses.napms(100)
        except:
            print("error occurred")
        curses.napms(3000)
        curses.endwin()

    def add_text(self, text):
        current_y, current_x = curses.getsyx()
        if(current_y >= self.height - 1):
            self.win.scroll(10)
            current_y = current_y - 10
        self.win.addstr(current_y + 1, 0, text)
        self.win.refresh()  # y,x coord of top left corner of pad in display; min y,x coord of screen; max y, x coord of screen

    def get_width(self):
        return self.screen.getmaxyx()[1]

    def get_height(self):
        return self.screen.getmaxyx()[0]

if __name__ == '__main__':
    GameWindow().play()
# mypad.chgat(i, 0, 10)


# while True:
#     c = win.getch()
#     y, x = curses.getsyx()
#     if c == ord('q'):
#         break  # Exit the while loop
#     elif c == curses.KEY_UP and y > 0:
#         win.chgat(y - 1, x, 10)
#         win.refresh()
#     elif c == curses.KEY_RIGHT and x < w-1:
#         win.chgat(y, x + 1, 10)
#         win.refresh()
#     elif c == curses.KEY_DOWN and y < h-1:
#         win.chgat(y + 1, x, 10)
#         win.refresh()
#     elif c == curses.KEY_LEFT and x > 0:
#         win.chgat(y, x - 1, 10)
#         win.refresh()
#
# wrapper(main)

