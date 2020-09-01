from gameWindow import GameWindow
import math, turtle

w = 40
game_window = GameWindow()
width = game_window.get_width()
height = game_window.get_height()
grid = []


def setup():
    cols = math.floor(width/w)
    rows = math.floor(height/w)

    for j in range(rows):
        for i in range(cols):
            cell = Cell(i, j)
            grid.append(cell)

    for p in range(grid.__len__()):
        grid[p].show()

class Cell():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self):
        x = self.i * w
        y = self.j * w
        if(self.walls[0]):
            turtle.pendown()
        else:
            turtle.penup()
        turtle.goto(x+w,y)
        if(self.walls[1]):
            turtle.pendown()
        else:
            turtle.penup()
        turtle.goto(x+w, y+w)
        if(self.walls[2]):
            turtle.pendown()
        else:
            turtle.penup()
        turtle.goto(x, y+w)
        if(self.walls[3]):
            turtle.pendown()
        else:
            turtle.penup()
        turtle.goto(x, y)

if __name__ == '__main__':
    setup()
