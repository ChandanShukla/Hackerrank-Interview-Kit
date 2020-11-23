import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    i=0
    j=0
    h=0
    k=0
    st=()
    temp=[0,0,0]
    while i<len(a):
        j=0
        while j<len(b):
            k=0
            while k<len(c):
                if a[i]<=b[j] and b[j]>=c[k]:
                    temp[0]=a[i]
                    temp[1]=b[j]
                    temp[2]=c[k]
                    print("temp:",temp)
                    if temp not in st:
                        st=st+(temp)
                        print("st:", st)
                k+=1
            j+=1
        i+=1
    print("st last:",st)
    return len(st)/3
if __name__ == '__main__':


    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    
    print(ans)

    
