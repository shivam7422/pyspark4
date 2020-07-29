'''It is a process which is used to change the existing functionality of the program
for ex- if we are going to divide two numbers what ever the numbers we give, it will take the
higher number as neumerator and the smaller one as denominator'''

def div(a,b):
    print(a/b)
'''in this we have to add another function and in that we have to write another funtion and that new function
 will take the same amount of input which the main function has taken'''
def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


div= smart_div(div)

div(2,4)