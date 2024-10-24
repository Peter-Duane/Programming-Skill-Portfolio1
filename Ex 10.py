    # -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:48:41 2024

@author: Peter Duane
"""
def num (): # defines num as the function that will execute once called.
   number = int(input("Enter your number: ")) # a variable that asks the user for their preffered number.
   if (number%2==0): # this if statement tests if the number given is divisible by two. In which if there is a remainder, then it will not be equal to zero.
                  # for example: if 15 is divided by 2, the answer will be 7 but there is still a remainder which is 1 so it will look something like: (1 != 0)
                  # this will trigger the function which will either be True (if even) or False (if odd).
        print("number is even")
   else: # this triggers if the number is odd.
        print ("number is odd")
    

num() # call the function