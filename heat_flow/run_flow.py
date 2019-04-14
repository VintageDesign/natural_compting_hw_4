#!/usr/bin/env python3
import argparse
from heat_flow import HeatFlow

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

def main(args):
    print(args)
    '''
    heatFlow= HeatFlow(
        args.ticks,
        args.x_size,
        args.y_size
    )

    heatFlow.run()
    '''

    '''
    TODO
    init heat flow with:
    y = linspace(0,10, y_size)
    grid[:, 0] = y(y-10)
    '''


if __name__ == "__main__":
    main(parse_args())
