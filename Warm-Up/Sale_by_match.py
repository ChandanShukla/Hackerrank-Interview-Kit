import math
import os
import random
import re
import sys
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique={}
    su=0
    for i in ar:
        if i not in unique.keys():
            unique[i]=1
        elif i in unique.keys():
            unique[i]+=1
    for i in unique.keys():
        if unique[i]>=2:
            su+=(unique[i]/2)
    return int(su)
if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
