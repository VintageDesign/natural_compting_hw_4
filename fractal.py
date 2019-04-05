import turtle
from time import sleep

T = turtle.Turtle()

def drawTree(level, size):
    """level = number of layers further to go"""
    if level == 0:
        # Draw one tree
        T.forward(20*size)
        T.backward(10*size)
        T.left(45)
        T.forward(10*size)
        T.backward(10*size)
        T.right(90)
        T.forward(10*size)
        T.backward(10*size)
        T.left(45)
        T.backward(10*size)
        return
    T.forward(20*size)
    drawTree(level-1, size/3)
    T.backward(10*size)
    T.left(45)
    T.forward(10*size)
    drawTree(level-1, size/3)
    T.backward(10*size)
    T.right(90)
    T.forward(10*size)
    drawTree(level-1, size/3)
    T.backward(10*size)
    T.left(45)
    T.backward(10*size)


def main():
    T.hideturtle()
    T.speed(0)
    T.up()
    T.left(90)
    T.sety(-100)
    T.down()
    drawTree(5, 10)
    sleep(100)


if __name__ == '__main__':
    main()
