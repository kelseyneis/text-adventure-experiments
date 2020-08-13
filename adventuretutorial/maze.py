import curses
window = curses.initscr()

print(curses.has_colors())
window.addstr("hi")

