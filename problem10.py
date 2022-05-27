'''This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.'''
import random
res=0
count=0
def selectRandom(x):
    global res
    global count
    count+=1 
    print(count)
    if(count==1):
        res=x 
    else:
        i=random.randrange(count)
        if(i==count-1):
            res=x 
    return res
stream = [1, 2, 3, 4];
n = len(stream);
 
for i in range (n):
    print("Random number from first",
         (i + 1), "numbers is",
          selectRandom(stream[i]));