#!/usr/bin/env python3
import argparse
from dol_systems import Example_A

def parse_args():
    parser = argparse.ArgumentParser(description="DOL creator")

    parser.add_argument(
        "--name",
        "-n",
        default=1,
        help="The name of the figure to save")
    parser.add_argument(
        "--tier",
        "-t",
        default=1,
        type=int,
        help="The number of iterations")
    parser.add_argument(
        "--dell",
        "-d",
        default=30,
        type=float,
        help="Angle of change")
    parser.add_argument(
        "--base",
        "-b",
        default='F',
        help="Base character")
    parser.add_argument(
        "--size",
        "-s",
        default=20,
        type=int,
        help="The size of the lines")
    return parser.parse_args()


def main(args):
    print(args)
    dol = Example_A(
            args.tier,
            args.dell,
            args.base,
            args.size,
            args.name
    )

    dol.run()


if __name__ == "__main__":
    main(parse_args())
