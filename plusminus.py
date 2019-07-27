#!/bin/python3
#Find how many no of positive,negative,zero's in givenarray.and Find Decimal value of this 
import math
import os
import random
import re
import sys

from decimal import Decimal
# Complete the plusMinus function below.
def plusMinus(arr):

    length=len(arr)
    pos=len(list(filter(lambda x:x>0, arr)))
    neg=len(list(filter(lambda x:x<0, arr)))
    zero=length-(pos+neg)
    print(Decimal(pos)/Decimal(length))
    print(Decimal(neg)/Decimal(length))
    print(Decimal(zero)/Decimal(length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
plusMinus(arr)