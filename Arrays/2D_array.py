

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    ma=-99999999
    for j in range(4):
        for i in range(4):
            su=arr[j][i]+arr[j][i+1]+arr[j][i+2]+arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
            ma=max(su,ma)
    return ma
if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print("Result: ",result)
