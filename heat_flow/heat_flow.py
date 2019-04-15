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
        self.grid[:, 0] = -y * (y - 10)


    def updateFlow(self):
        new_grid = np.zeros(self.grid_size)
        for i in range(1, self.grid_size[0]-1-1):
            #new_grid[i][0] = self.grid[i-1][0]
            #new_grid[i,self.grid_size[1]-1] = self.grid[i-1, self.grid_size[1]-1]
            for j in range(1, self.grid_size[1]-2):
                print(j)
                new_grid[i,j] = round((self.grid[i-1, j] + self.grid[i+1, j] + self.grid[i, j-1] + self.grid[i, j+1])/4)
        self.grid = new_grid


    def showGrid(self):
        '''
        Prints the grid
        '''
        image = plt.imshow(self.grid, cmap='Greys')
        plt.show()


    def run(self):
        return_list = []
        for iteration in range(0, self.ticks):
            self.updateFlow()
            if iteration % round(self.ticks/9) == 0:
                return_list.append(self.grid)
        return return_list

