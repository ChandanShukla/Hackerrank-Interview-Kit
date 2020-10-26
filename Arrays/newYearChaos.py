
if __name__ == '__main__':
    T=int(input().split())
    arr=[]
    for i in range(T):
        sum1=0
        temp=int(input().rstrip())
        while temp!=0:
            sum1+=temp%10
            temp=int(temp/10)  
        arr.append(sum1)
    
    for j in range(T):
        print(arr[j])
        
        