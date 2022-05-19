'''Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.'''
s=input()
n=len(s)
if s[0]=='0':
    print(0)
if n==1:
    print(1)
current=1 
prev=1 
for i in range(1,n):
    sValue=0
    if(s[i]!='0'):
        sValue=current
    
    if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
        sValue+= prev
            
    prev = current
    current = sValue
print(current)