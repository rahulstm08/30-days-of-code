import math
import os
import random
import re
import sys
def solve(meal_cost, tip_percent, tax_percent):
    x=tip_percent/100*meal_cost
    y=tax_percent/100*meal_cost
    print(round(x+y+meal_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
