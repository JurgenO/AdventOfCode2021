# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 07:26:20 2021

@author: jurge

Solution to Advent of Code 2021 day 5:   
    "You come across a field of hydrothermal vents ... "
 
0,9 -> 5,9 -> ok
8,0 -> 0,8
9,4 -> 3,4 -> ok
2,2 -> 2,1 -> ok
7,0 -> 7,4 -> ok
6,4 -> 2,0
0,9 -> 2,9 -> ok
3,4 -> 1,4 -> ok
0,0 -> 8,8 
5,5 -> 8,2

"""


# Part 1

import matplotlib.pyplot as plt
import numpy as np

with open("Advent2021_Day5.txt") as inFile: 
    data = inFile.read().split("\n")
    # print (data)

    
    big_list_coords = [[0,0]]
    big_list_coords.pop()

    for element in data:
        # print(element)
        coord1, coord2 = element.split("->")
        # print ("Coord 1: ", coord1)
        # print ("Coord 2: ", coord2)
        x1_str,y1_str = coord1.split(",")
        x2_str,y2_str = coord2.split(",")
        x1=int(x1_str)
        y1=int(y1_str)
        x2=int(x2_str)
        y2=int(y2_str)
        
        
        line=[[x1,y1],[x2,y2]]        
        print(line)
        

# Expand the line
        if (x1 == x2):
            print ("Horizontal expansion") 
            if (y2 > y1): 
                for dot in range(y2-y1+1): 
                    big_list_coords.append([x1, dot+y1]) 
            if (y1 > y2): 
                for dot in range(y1-y2+1): 
                    big_list_coords.append([x1, dot+y2]) 
           
            
            
        elif (y1 == y2): 
            print ("Vertical expansion")
            if (x2 > x1):
                for dot in range(x2-x1+1):
                    big_list_coords.append([dot+x1,y1])
            if (x1 > x2):
                for dot in range(x1-x2+1):
                    big_list_coords.append([dot+x2,y1])
           
            
        else:
            '''
            Uncomment for first part
            print ("Line skipped !")
            '''
            print ("Diagonal expansion")
            
            if(x1<x2):
                print("x1 < x2 ! From x1 to x2")
                if (y1<y2):
                    print("y1 < y2 ! Count from y1 to y2")
                    for dot in range(x2-x1+1):
                        big_list_coords.append([x1+dot,y1+dot])
                else:
                    print("y1 > y2 ! Count from y2 to y1")
                    for dot in range(x2-x1+1):
                        big_list_coords.append([x1+dot,y1-dot])
                    
            else:
                print("x1 > x2 ! From x2 to x1")
                if (y1<y2):
                    print("y1 < y2 ! Count from y1 to y2")
                    for dot in range(x1-x2+1):
                        big_list_coords.append([x1-dot,y1+dot])
                else:
                    print("y1 > y2 ! Count from y2 to y1")
                    for dot in range(x1-x2+1):
                        big_list_coords.append([x1-dot,y1-dot])
                
            
            
            

    
   

    # convert to str and plot
    # fig, ax = plt.subplots()  # Create a figure containing a single axes.
    big_list_coords_str = [" "]
    big_list_coords_str.pop()
    
    for coord in big_list_coords:
        print (coord)
        big_list_coords_str.append(str(coord[0])+"-"+str(coord[1]))
        

      #   ax.plot(coord[0],coord[1],marker="x", markersize=20, markeredgecolor="red", markerfacecolor="green")


    # plt.show()


    dict_coords = {i:big_list_coords_str.count(i) for i in big_list_coords_str}

    number_of_duplicates = 0 
    for j in dict_coords:
        if dict_coords[j] > 1:
            number_of_duplicates = number_of_duplicates +1
        # print (dict_coords[j])

    print (number_of_duplicates)



# The answer of the second part is: 17717






'''
Tipps and Tricks
https://matplotlib.org/stable/tutorials/introductory/usage.html
https://docs.python.org/3/tutorial/datastructures.html
https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list
'''

