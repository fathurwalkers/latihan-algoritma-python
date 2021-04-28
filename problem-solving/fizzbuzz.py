import os 
import sys 
import math 
import array

def fizzbuzz(total):
    for i in range(total):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz") 
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
    
fizzbuzz(100)