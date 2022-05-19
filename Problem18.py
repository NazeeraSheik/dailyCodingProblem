'''Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7) '''
arr=list(map(int,input().split()))
k=int(input())
m=0
for i in range(0,len(arr)-k+1):
    m=arr[i]
    for j in range(1,k):
        if(arr[i+j]>m):
            max=arr[i+j]
    print(str(m) + " ", end ="")