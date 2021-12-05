# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:26:20 2021

@author: jurge

Solution to Advent of Code 2021 day 3
Very much based on Stefan Bisplinghoff's solutions of 2020 and 2021

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010


Hint 1 available here: https://stackoverflow.com/questions/29629315/import-text-file-as-matrix-in-numpy
Use numpy.loadtxt, which assumes the data are delimited by whitespace by default and takes an argument usecols specifying which fields to use in building the array:

In [1]: import numpy as np
In [2]: matrix = np.loadtxt('matrix.txt', usecols=range(7))
In [3]: print matrix

Hint 2 https://stackoverflow.com/questions/13567345/how-to-calculate-the-sum-of-all-columns-of-a-2d-numpy-array-efficiently


"""


# Part 1

import numpy as np


# Note : I had to modify the input file with a text editor: 
# replace "1" by "1 " and "0" by "0 "

# atrix = np.loadtxt('Advent2021_Day3Easy.txt', usecols=range(5))
matrix = np.loadtxt('Advent2021_Day3.txt', usecols=range(12))
print (matrix)

# Summarise the values over the columns
sum_over_columns = matrix.sum(axis=0)
print (sum_over_columns)

# How many elements has one column, i.e. how many rows ?
num_rows, num_cols = matrix.shape
print (num_rows)
print (num_cols)

# Each bit in the gamma rate can be determined by finding the 
# most common bit in the corresponding position of all numbers in the diagnostic report.
# Build the gamma rate as string
# Note that epsilon_rate is the exact opposite

gamma_rate = ""
epsilon_rate = ""

for position in range(num_cols):
    print (sum_over_columns[position])
    if (sum_over_columns[position]>num_rows/2):
        gamma_rate = gamma_rate + "1"
        epsilon_rate = epsilon_rate + "0"
    else:
        gamma_rate = gamma_rate + "0"
        epsilon_rate = epsilon_rate + "1"

print (gamma_rate)
print (epsilon_rate)

gamma_rate_int = int(gamma_rate, 2)
epsilon_rate_int = int(epsilon_rate, 2)

print (gamma_rate_int)
print (epsilon_rate_int)

print ("Part 1 result = ", gamma_rate_int * epsilon_rate_int )


# Part 2 ... to be done

            








