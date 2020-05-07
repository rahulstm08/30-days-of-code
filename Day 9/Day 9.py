
import math
import os
import random
import re
import sys

def factorial(n):
    f=n;
    if n==1:
        return f
    else:
        return (f*factorial(n-1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
