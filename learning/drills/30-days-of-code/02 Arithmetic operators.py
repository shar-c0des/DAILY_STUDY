import math 
import os 
import random 
import re 
import sys 



def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    tip = tip_percent * meal_cost
    taxes = tax_percent * meal_cost 

    print(tip)
