#!/usr/bin/env python3
import argparse
from dol_systems import Example_A
from dol_systems import Example_B
from dol_systems import Example_C
from dol_systems import Example_D
from dol_systems import Example_E
from dol_systems import Example_F

# args = Tier, dell, base, size, file_name



def main():
    print('Running B')
    dol = Example_B(
            4, #4
            22.5,
            'F',
            6,
            "Example_B"
    )
    dol.run()
    print('Running D')
    dol = Example_D(
            9,
            20,
            'G',
            .5,
            "Example_D"
    )
    dol.run()
    print('Running E')
    dol = Example_E(
            9,
            25.7,
            'G',
            .5,
            "Example_E"
    )
    dol.run()
    print('Running F')
    dol = Example_F(
            5,
            22.5,
            'G',
            7,
            "Example_F"
    )
    dol.run()

if __name__ == "__main__":
    main()
