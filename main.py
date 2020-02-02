#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    difffromarr = [0]*(n+1)
    maxarr = [0]*n
    for i in range(len(queries)):
        difffromarr[queries[i][0]-1] += queries[i][2]
        difffromarr[queries[i][1]] -= queries[i][2]
    for i in range(n):
        if i ==0:
            maxarr[0] = difffromarr[0]
            continue
        maxarr[i]=maxarr[i-1]+difffromarr[i]
    # print(maxarr)
    return max(maxarr)

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)
