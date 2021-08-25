#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    a=[]
    for j in range(0,n):
        if ar[j] not in a:
            a.append(ar[j])
    count=0
    for i in range(0,len(a)):
        x=ar.count(a[i])
        if x%2==0:
            count=count+(x//2)
        else:
            count=count+((x-1)//2)
    return count
        
    
    
        
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
