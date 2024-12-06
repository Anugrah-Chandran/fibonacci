'''Author:Anugrah Chandran
Date:6-12-24
Description:Program to define a module to find Fibonacci Numbers and import the module to another program'''
def fibonacci_number(num):
    fib=[]
    first_number = 0
    next_number = 1
    for i in range(num):
        fib.append(first_number)
        first_number,next_number=next_number,first_number+next_number

    return fib







