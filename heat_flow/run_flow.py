#!/usr/bin/env python3
import argparse
from heat_flow import HeatFlow
import pylab as plt

def parse_args():
    parser = argparse.ArgumentParser(description="DOL creator")

    parser.add_argument(
        "--ticks",
        "-t",
        default=1,
        type=int,
        help="Iterations to run")
    parser.add_argument(
        "--x_size",
        "-x",
        default=20,
        type=int,
        help="X size of the grid")
    parser.add_argument(
        "--y_size",
        "-y",
        default=20,
        type=int,
        help="Y size of the grid")
    return parser.parse_args()

def main(args):
    print(args)
    heatFlow= HeatFlow(
        args.ticks,
        args.x_size,
        args.y_size
    )

    results = heatFlow.run()

    for i in range(0,9):
        print(i)
        plt.subplot(3,3, i+1)
        plt.imshow(results[i], cmap=plt.cm.gray , interpolation='nearest')

    plt.show()


if __name__ == "__main__":
    main(parse_args())
