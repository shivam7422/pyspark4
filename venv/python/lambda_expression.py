''' A function which takes one expression, multiple argument,less codes ew'''
from functools import reduce
f= lambda x:x+2
print(f(2))

nums= [3,2,6,8,4,2,9]
evens= list(filter(lambda x: x%2 ==0,nums))
double= list(map(lambda x: x*2,nums))
red= reduce(lambda a,b:a+b, nums)
print(evens)
print(double)
print(red)