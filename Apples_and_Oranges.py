#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(0,m):
        apples[i]=a+apples[i]
    for j in range(0,n):
        oranges[j]=b+oranges[j]
    applecount=0
    orangecount=0
    for k in range(0,m):
        if apples[k]>=s and apples[k]<=t:
            applecount=applecount+1
    for l in range(0,n):
        if oranges[l]>=s and oranges[l]<=t:
            orangecount=orangecount+1
    print(applecount)
    
    print(orangecount)
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
