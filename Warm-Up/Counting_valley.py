import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    count=0
    mi=0
    valley=0
    for i in range(steps):
        if path[i]=='U':
            count+=1
            if count==0 and mi==-1:
                valley+=1
            mi=count
        elif path[i]=='D':
            count+=-1
            if mi>count:
                mi=count
    return valley

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)