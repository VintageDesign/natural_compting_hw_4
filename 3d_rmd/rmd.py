from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal, seed

H = 0.7                 # H value, higher = smoother
selfSimilar = False     # Set to True to make fractals self-similar
level = 7               # Levels of recursion to do
randSeed = 9            # Seed for the RNG
sigma = 1
N = 2**level


def recursion(x, t1, t9, t, level, delta):
    """
    x = 2D array of height values
    t1, t9 = corners of working space
    Looks like
        t1 t2 t3
        t4 t5 t6
        t7 t8 t9
    t = current recursion level
    level = max level of recursion
    delta = array of perturbation strengths for each level
    """
    if (selfSimilar):
        # This will cause every subsection to resemble the whole shape
        seed(randSeed)

    # Calculate locations of t2-t8
    t2 = ((t1[0]+t9[0])//2, t1[1])
    t3 = (t9[0], t1[1])
    t4 = (t1[0], (t1[1]+t9[1])//2)
    t5 = ((t1[0]+t9[0])//2, (t1[1]+t9[1])//2)
    t6 = (t9[0], (t9[1]+t1[1])//2)
    t7 = (t1[0], t9[1])
    t8 = ((t1[0]+t9[0])//2, t9[1])

    # Perturb the 5 inner locations
    x[t2] = 0.5 * (x[t1] + x[t3]) + normal(0, delta[t])
    x[t4] = 0.5 * (x[t1] + x[t7]) + normal(0, delta[t])
    x[t6] = 0.5 * (x[t3] + x[t9]) + normal(0, delta[t])
    x[t8] = 0.5 * (x[t7] + x[t9]) + normal(0, delta[t])
    x[t5] = 0.25 * (x[t2] + x[t4] + x[t6] + x[t8]) + normal(0, delta[t])

    if t < level-1:
        # Run on the four resulting smaller squares
        recursion(x, t1, t5, t+1, level, delta)
        recursion(x, t2, t6, t+1, level, delta)
        recursion(x, t4, t8, t+1, level, delta)
        recursion(x, t5, t9, t+1, level, delta)


def main():
    z = np.zeros((N+1, N+1))
    seed(randSeed)

    # Initialize corners of z
    z[0, N] = sigma*normal(0, sigma)
    z[N, 0] = sigma*normal(0, sigma)
    z[N, N] = sigma*normal(0, sigma)

    # Get perturbation amounts
    delta = []
    for i in range(level):
        delta.append(sigma * (0.5**((i+1)*H)))

    # Generate the z values
    recursion(z, (0, 0), (N, N), 0, level, delta)

    # Plot in 3D
    x = np.linspace(0, 2**level+1, 2**level+1)
    y = np.linspace(0, 2**level+1, 2**level+1)
    X, Y = np.meshgrid(x, y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, z, cmap='viridis', linewidth=0, antialiased=False)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    plt.show()


if __name__ == '__main__':
    main()