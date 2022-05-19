arr=list(map(int,input().split()))
dict={}
flag=0
k=int(input())
for i in range(0,len(arr)):
    m=k-arr[i]
    if m in dict:
        print("true")
        flag=1
        break
    else:
        dict[arr[i]]=i
if(flag==0):
    print("false")