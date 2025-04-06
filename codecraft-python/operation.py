'''18. Create operation.py file which contain all arithmetic operations. Then create calculate.py file 
and perform all these operation from operation.py file''' 
# operation.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error!"
    return a / b
