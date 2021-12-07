# -*- coding: utf-8 -*-
"""

@author: jurge
Solution to Advent of Code 2021 day 6
"""


# Part 1


fishday=[]


with open("Advent2021_Day6Easy.txt") as inFile: 
    initial = inFile.read().split(",")
    for i in range(len(initial)):
        print(i)
        fishday.append ([i, int(initial[i])])
    
 
    for day in range(257): # set range to 81 for part 1
        # print status
        print ("After day " + str(day) +  ": ", end = '')
        #for fish in fishday:
            #   print(str(fish[1]) + ",", end = '' )
        print()    
        print ("Number of fish:", len(fishday))
        

    
        for fish in fishday:
            # print (fish[1])
            fish[1] = fish[1] - 1 # reduce the lifetime
    
        for fish in fishday:
            if fish[1] == -1:
                fish[1] = 6 # reset parent fish lifetime
                fishday.append([len(fishday),8])

   


# Part 2
'''
For part 2 1 ran the script with 257 days

    for day in range(257):

Even with the 5 inputs provided in the example the script did take 
forever and exited with an error message        
    After day 221: 
    Number of fish: 1275457000
    After day 222: 
    Number of fish: 1396116848
    Traceback (most recent call last):

        File "C:\Users\jurge\PythonProjekte\002_Advent2021\Day_06\Advent2021_Day6.py", line 39, in <module>
    fishday.append([len(fishday),8])

    MemoryError
    
    
    So I did not even try running the script with the actual input