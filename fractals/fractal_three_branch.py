import turtle
import random
from time import sleep

angle = 45


def drawTree(level, size, T, color):
    """level = number of layers further to go"""
    if level == 0:
        return

    T.color(str(hex(color)))



    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    next_layer_color = r << 16 + g << 8 + b

    T.forward(size)
    T.left(angle)
    drawTree(level - 1, size/3, T, next_layer_color)
    T.right(2*angle)
    drawTree(level - 1, size/3, T, next_layer_color)
    T.left(angle)
    drawTree(level - 1, size/3, T, next_layer_color)
    T.backward(size)



def main():
    T = turtle.Turtle()
    T.hideturtle()
    T.speed(0)
    T.up()
    T.left(90)
    T.sety(-400)
    T.down()
    drawTree(5, 300, T, int(FFFFFF))
    ts = turtle.getscreen()

    ts.getcanvas().postscript(file="fractal.eps")
    turtle.clearscreen()


if __name__ == '__main__':
    main()
