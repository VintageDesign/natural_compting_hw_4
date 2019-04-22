#!/bin/bash

gcc -o greyscott greyscott.c
./greyscott
gnuplot -e "set terminal emf;set output \"out.emf\";set contour;unset surface;unset ztics;unset zlabel;set view map;splot \"gsuData.txt\" matrix with lines"
