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
    print('Running A')
    dol = Example_A(
            8, #8
            22.5,
            'G',
            1,
            "Example_A"
    )
    dol.run()
    print('Running B')
    dol = Example_B(
            4, #4
            22.5,
            'F',
            1,
            "Example_B"
    )
    dol.run()
    print('Running C')
    dol = Example_C(
            6,
            22.5,
            'G',
            1,
            "Example_C"
    )
    dol.run()
    print('Running D')
    dol = Example_D(
            9,
            20,
            'G',
            1,
            "Example_D"
    )
    dol.run()
    print('Running E')
    dol = Example_E(
            9,
            25.7,
            'G',
            2,
            "Example_E"
    )
    dol.run()
    print('Running F')
    dol = Example_F(
            5,
            22.5,
            'G',
            2,
            "Example_F"
    )
    dol.run()

if __name__ == "__main__":
    main()
