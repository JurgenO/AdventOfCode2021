# -*- coding: utf-8 -*-
"""

@author: jurge
Solution to Advent of Code 2021 day 7
"""


# Part 1

import statistics as stat

with open("Advent2021_Day7.txt") as inFile: 
    crab_position_str = inFile.read().split(",")
    
    crab_position = []
    
    for i in range(len(crab_position_str)):
        crab_position.append(int(crab_position_str[i]))
    
    print(crab_position)
    


    best_pos = stat.median(crab_position)
    
    print (best_pos)
   

    fuel = 0
    for i in range(len(crab_position)):
        if crab_position[i] > best_pos:
            fuel = fuel + crab_position[i] - best_pos
        else:
            fuel = fuel - crab_position[i] + best_pos
        

    print (fuel)

# Answer 343468


# Part 2
    
    print ("Mean:", stat.mean(crab_position))
   
    
    best_pos = int(stat.mean(crab_position))
    # best_pos =  478   # This is the correct answer

    fuel = 0
    for i in range(len(crab_position)):
        if crab_position[i] > best_pos:
            for step in range (crab_position[i] - best_pos):
                fuel = fuel + step +1
            
        else:
            for step in range (-crab_position[i] + best_pos):
                fuel = fuel + step +1
            
        

    print (fuel)


# Answer 96086265

