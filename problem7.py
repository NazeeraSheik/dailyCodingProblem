'''This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.'''
import random
INTERVAL=1000


inside_circle_points=0 
inside_square_points=0 


for i in range(INTERVAL**2):
    rand_x=random.uniform(-1,1)
    rand_y=random.uniform(-1,1)
    origin_dist=rand_x**2+rand_y**2
    if(origin_dist<=1):
        inside_circle_points+=1 
    inside_square_points+=1 
    pi=4*inside_circle_points/inside_square_points
print(pi)