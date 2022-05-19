'''For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''
arr=list(map(int,input().split()))
n=len(arr)
if n==1:
    print(*arr)
else:
    leftArr=[0]*n 
    rightArr=[0]*n 
    result=[0]*n
    leftArr[0]=1 
    rightArr[n-1]=1 
    for i in range(1,n):
        leftArr[i]=arr[i-1]*leftArr[i-1]
    for j in range(n-2,-1,-1):
        rightArr[j]=arr[j+1]*rightArr[j+1]
    for i in range(n):
        result[i] = leftArr[i]*rightArr[i]
    for i in range(n):
        print(result[i],end =' ')
 
    