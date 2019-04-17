import turtle
from time import sleep




def drawTree(level, size, T, angle):
    """level = number of layers further to go"""
    if level == 0 :
        return

    T.forward(size)
    T.left(angle)
    drawTree(level - 1, size/3, T, angle)
    T.right(2*angle)
    drawTree(level - 1, size/3, T, angle)
    T.left(angle)
    drawTree(level - 1, size/3, T, angle)
    T.backward(size)



def main():
    for angle in range( 45, 120):
        T = turtle.Turtle()
        T.hideturtle()
        T.speed(0)
        T.up()
        T.left(90)
        T.sety(-400)
        T.down()
        drawTree(5, 300, T, angle)
        ts = turtle.getscreen()

        ts.getcanvas().postscript(file="fractal_" + str(angle) + ".eps")
        turtle.clearscreen()



if __name__ == '__main__':
    main()
