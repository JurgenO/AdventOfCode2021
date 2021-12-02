# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:26:20 2021

@author: jurge
"""




# Solution to Advent of Code 2021 day 2
# Very much based on Stefan Bisplinghoff's solutions of 2020 and 2021
#
#
# forward 5   # command - value
# down 5
# forward 8
# up 3
# down 8
# forward 2

# Part 1
Position_horizontal = 0
depth = 0
    
with open("Advent2021_Day2.txt") as inFile: 
    data = inFile.read()

    for field in data.split("\n"):
        # print ("Field: " + field)              
        command = field.split (" ")
        # print ("Command: ")
        # print (command)
        # print (command[0])
        # print (command[1])
        value = int(command[1])
        if command[0] == "forward":
            Position_horizontal = Position_horizontal + value
        elif command[0] == "down":
            depth =  depth + value 
        elif command[0] == "up":
            depth =  depth - value
             
        print(Position_horizontal)                 
        print(depth)                 
                         
    print("Result")                       
    print(Position_horizontal*depth)
                         
                        

# Part 2
Position_horizontal = 0
depth = 0
aim = 0
    
with open("Advent2021_Day2.txt") as inFile: 
    data = inFile.read()

    for field in data.split("\n"):
        # print ("Field: " + field)              
        command = field.split (" ")
        # print ("Command: ")
        # print (command)
        # print (command[0])
        # print (command[1])
        value = int(command[1])
        


        
        if command[0] == "forward":
            # forward X does two things:
            # It increases your horizontal position by X units.
            # It increases your depth by your aim multiplied by X.
            Position_horizontal = Position_horizontal + value
            depth = depth + value * aim
        elif command[0] == "down":
            aim =  aim + value   # down X increases your aim by X units.
        elif command[0] == "up":
            aim =  aim - value # up X decreases your aim by X units.
             
        print(Position_horizontal)                 
        print(depth)                 
                         
    print("Result")                       
    print(Position_horizontal*depth)
                         


