'''This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.'''


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
)
## here what happens is that when we called the function cons using variables it returns an another function pair..and then pair will be called which have access to the variables a,b using closure namespace its like they are under local namespace then it returns an function f with arguments a and b .here f(a,b) is an pair object returned by function pair

##here f can be anything
##lets see how this will work
f = lambda n, m: n+m
car = lambda n, m: n
cdr = lambda n, m: m
k=cons(2,3)(f)
p=cons(2,3)(car)
q=cons(2,3)(cdr)

print(k)
print(p)
print(q