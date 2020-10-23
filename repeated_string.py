
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count=0
    for i in range(len(s)):
        if s[i]=='a':
            count+=1
    no_a=int((n/len(s)))*count
    rem=n%len(s)
    for j in range(rem):
        if s[j]=='a':
            no_a+=1
    return no_a
if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    
    print(result)

    