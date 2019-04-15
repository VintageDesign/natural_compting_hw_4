import numpy as np
import pylab as plt

class HeatFlow:
    def __init__(self, ticks, x_size, y_size):
        '''
        :param ticks  - the number of iterations to run
        :param x_size - the grid's x length
        :param y_size - the grid's y length
        '''

        self.ticks = ticks
        self.grid_size = (x_size, y_size)

        self.grid = np.zeros(self.grid_size)
        y = np.linspace(0,10, y_size)
        self.grid[:, 0] = y * (y - 10)


    def updateFlow(self):
        new_grid = np.zeros(self.grid_size)
        for i in range(1, self.grid_size(0)):
            for j in range(0, self.grid_size(1)):
                new_grid[i,j] = self.grid[i-1, j]

    def showGrid(self):
        '''
        Prints the grid
        '''
        image = plt.imshow(self.grid, cmap='Greys')
        plt.show()


    def run(self):
        return_list = []
        for iteration in range(0, self.ticks):
            self.update_flow()
            if iteration % 100 = 0:
                return_list.append(self.grid)
        return return_list

