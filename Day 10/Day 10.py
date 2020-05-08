#!/bin/python3

import math
import os
import random
import re
import sys


def DecimalToBinary(num,maxx,c):
    if num >= 1:
        d=num%2
        #print(d)
        if d==1:
            c+=1
            if maxx < c:
                maxx=c                
        else: 
            c=0
        DecimalToBinary(num // 2,maxx,c)
    else:
        print(maxx)
        

if __name__ == '__main__':
    n = int(input())
    maxx=0
    c=0
    DecimalToBinary(n,maxx,c)
    
