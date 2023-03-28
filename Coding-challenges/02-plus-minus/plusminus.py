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

def calculate_ratios(arr):
    pos, neg, zero = 0, 0, 0
    n = len(arr)

    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    pos_ratio = pos / n
    neg_ratio = neg / n
    zero_ratio = zero / n

    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))

def plusMinus(arr):
    calculate_ratios(arr)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
