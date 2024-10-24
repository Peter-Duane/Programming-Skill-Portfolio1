    # -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:25:55 2024

@author: Peter Duane
"""

"""
Exercise 5 = Days of the Month
"""

month = {1:31, 
         2:28,
         3:31,
         4:30,
         5:31,
         6:30,
         7:31,
         8:31,
         9:30,
         10:31,
         11:30,
         12:31
         } # dictionary of months and their respective days.
m=int(input("How many days in a month? ")) # interacts with the user and asks for their preferred number.

if 1 <= m <= 12: # the program should recognize that if the number typed by the user is valid which is less or equal to 12.
   if m == 2:
       leap_year=(input("Leap year? Yes/No: ")).lower()
       if leap_year == 'yes':
           print("Month 2 has 29 days")
       else:
           print("Month 2 has 28 days")
   else:
       print("There are" , month[m], "days in month", m) # month[m] reiterates the values in the dictionary, while the "m" reiterates the keys in the dictionary.
else: # if the number is higher than 12, it won't be valid.
   print("Invalid input")