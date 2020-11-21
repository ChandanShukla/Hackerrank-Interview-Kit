import math
import os
import random
import re
import sys

def rotLeft(a, d):
    ar=[]
    i=d
    j=0
    while i<len(a):
        ar.append(a[i])
        i+=1
    i=0
    while i<d:
        ar.append(a[i])
        i+=1
    k=0
    str1=""
    count=0
    for i in ar:
        str1+=str(i)
        if count<len(ar)-1:
            str1+=" "
    return str1

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print (result)