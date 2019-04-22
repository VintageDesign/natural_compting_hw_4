import turtle
import random
from time import sleep

angle = 85



def drawTree(level, size, T, color):
    """level = number of layers further to go"""
    if level == 0:
        return

    color_val = str(hex(color))[2:]
    while len(color_val) < 6:
        color_val = "0" + color_val

    T.color("#" + color_val )


    next_layer_color = random.randint(0, 16777215)


    T.forward(size)
    T.left(angle)
    drawTree(level - 1, size/3, T, next_layer_color)
    T.color("#" + color_val )
    T.right(2*angle)
    drawTree(level - 1, size/3, T, next_layer_color)
    T.color("#" + color_val )
    T.left(angle)
    drawTree(level - 1, size/3, T, next_layer_color)
    T.color("#" + color_val )
    T.backward(size)



def main():
    T = turtle.Turtle()
    T.hideturtle()
    T.speed(0)
    T.up()
    T.left(90)
    T.sety(-400)
    T.down()
    drawTree(5, 300, T, int(0x111111))
    ts = turtle.getscreen()

    ts.getcanvas().postscript(file="fractal.eps")
    turtle.clearscreen()


if __name__ == '__main__':
    main()
