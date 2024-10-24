# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:24:38 2024

@author: Peter Duane
"""

"""
Exercise 7 = Some Counting
"""

i = 0 # create a variable that acts as the starting count

while i <= 50: # while the variable is less than or equal 50, the loop will execute.
    print(i)   # prints the current variable.
    i += 1     # adds one increment to the variable as long as it has not reached 50. 
               # but when the variable does reach 50, the loop terminates.

print("________________")

i = 50         # in this case, starting count will start at a larger number which will then decrease to 0

while i >= 0:
    print(i)   
    i -= 1     # the variable will decrease in decrements of 1. when the variable reaches the certain number, the loop ends.
    
    
print("________________")

i = 30

while i <= 50:
    print(i)
    i += 1     # the variable increases by 1 and will stop when it reaches 50
    
print("________________")
    
i = 50
while i >= 10: 
    print(i)
    i -= 2     # the variable decreases by 2 and will stop when it is equal to 10
    
print("________________")

i = 100
while i <= 200:
    print(i)
    i += 5     # the variable increases by 5 and will stop when it is less than or equal to 200
    
    
    
    
    
    
    
    
    
    
    
    