# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 03:03:07 2024

@author: Santosh
"""
import random

n = input("enter the number you want to check with")


x = 0
for i in range(100000):
    dice_roll1 = random.choice([1, 2, 3, 4, 5, 6])
    dice_roll2 = random.choice([1, 2, 3, 4, 5, 6])
    dice_roll3 = random.choice([1, 2, 3, 4, 5, 6])
    dice_sum1 = int(dice_roll1) + int(dice_roll2)
    if dice_sum1 % int(n) == 0:
        x += 1
    else:
        x = x
        
    
print("the chance that sum of 3 dice is divisible by " + 
      str(n) + " is approximately" + str(x/1000))
    
        
        
        