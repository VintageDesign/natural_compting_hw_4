import numpy as np
import pylab as plt
from math import ceil

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
        self.grid[:, 0] = -y * (y - 10)


    def updateFlow(self):
        new_grid = np.zeros(self.grid_size)
        new_grid[:,:] = self.grid[:,:]
        for col in range(1, self.grid_size[1] - 1):
            new_grid[0,col] = self.grid[0,col-1]
            new_grid[self.grid_size[0]-1,col] = self.grid[self.grid_size[0]-1,col-1]
        for j in range(1, self.grid_size[1]-1):
            for i in range(0, self.grid_size[0]-1):
                new_grid[2i,j] = (self.grid[i-1, j] + self.grid[i+1, j] + self.grid[i, j-1] + self.grid[i, j+1])/4
        self.grid[:,:] =  new_grid[:,:]


    def showGrid(self):
        '''
        Prints the grid
        '''
        image = plt.imshow(self.grid, cmap='Greys')
        plt.show()


    def run(self):
        return_list = [ np.copy(self.grid) ]
        for iteration in range(0, self.ticks):
            self.updateFlow()
            if iteration % ceil(self.ticks/9) == 0:
                print(iteration)
                return_list.append(np.copy(self.grid))
        return return_list

