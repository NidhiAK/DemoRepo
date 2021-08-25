#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus=minus=zero=0
    for i in range(0,n):
        if arr[i]<0:
            minus=minus+1
        elif arr[i]>0:
            plus=plus+1
        elif arr[i]==0:
            zero=zero+1
    print (plus/n)
    print (minus/n)
    print (zero/n)
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
