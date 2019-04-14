import numpy as np
from matplotlib.pyplot import imshow

class HeatFlow:
    def __init__(self, ticks, x_size, y_size):
        '''
        :param ticks  - the number of iterations to run
        :param x_size - the grid's x length
        :param y_size - the grid's y length
        '''

        self.ticks = ticks
        self.grid_size = (x_size, y_size)

        self.grid = np.zeros(grid_size)

    def show_grid(self):
        '''
        Prints the grid
        '''
        imshow(self.grid)


