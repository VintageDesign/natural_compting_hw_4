import turtle
from time import sleep

angle = 85



def drawTree(level, size, T):
    """level = number of layers further to go"""
    if level == 0 :
        return

    T.forward(size)
    T.left(angle)
    drawTree(level - 1, size/3, T)
    T.right(2*angle)
    drawTree(level - 1, size/3, T)
    T.left(angle)
    drawTree(level - 1, size/3, T)
    T.backward(size)



def main():
    T = turtle.Turtle()
    T.hideturtle()
    T.speed(0)
    T.up()
    T.left(90)
    T.sety(-400)
    T.down()
    drawTree(5, 300, T)
    sleep(100)


if __name__ == '__main__':
    main()
