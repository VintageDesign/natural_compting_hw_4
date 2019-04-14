import turtle
from time import sleep



class DOL(object):
    """
    Base class for all the DOL systems
    """
    def __init__(self, t_val, del_val, initial_char, size, name):
        """
        :param dell             = the rotation value for +,- characters
        :param layers           = the number of rewrites to do
        :param inital_character = the inital character to start the rewrites
                                  with
        :param T                = the turtle plot
        :param size             = the number of pixels to plot for each
                                  character
        """
        self.dell = del_val
        self.layers = t_val
        self.inital_character = initial_char
        self.size = size
        self.T = turtle.Turtle()
        self.name = name

        self.T.hideturtle()
        self.T.speed(0)
        self.T.up()
        self.T.left(90)
        self.T.sety(-400)
        self.T.down()


    def display_tier(self, structure):
        """
        Recursive method for printing the tree.
        Im sorry for any one who has to read this code.
        """
        stack = []

        while len(structure) > 0:
            character = structure.pop(0)
            # apply the stack in reverse to get back to the postion before '['
            if character == ']':
                while len(stack) > 0:
                    reverse_character = stack.pop()
                    if reverse_character == 'F' or reverse_character == 'G':
                        self.draw('R')
                    else:
                        reverse_character = '-' if reverse_character == '+' \
                                else '+'
                        self.draw(reverse_character)
                return
            # start a new stack
            elif character == '[':
                self.display_tier(structure)
            # Add to stack and draw the character
            else:
                stack.append(character)
                self.draw(character)



    def draw(self, character):
        '''
        Draws a single character
        '''

        if character == 'R':
            self.T.backward(self.size)
        elif character == 'F' or character == 'G':
            self.T.forward(self.size)
        elif character == '+':
            self.T.right(self.dell)
        else:
            self.T.left(self.dell)

    def run(self):
        structure = self.rewrite(self.inital_character)
        for x in range(self.layers - 1):
            structure = self.rewrite(structure)

        self.display_tier(structure)
        ts = turtle.getscreen()

        ts.getcanvas().postscript(file=self.name + ".eps")
        turtle.clearscreen()

    def rewrite(self, structure):
        raise NotImplementedError
