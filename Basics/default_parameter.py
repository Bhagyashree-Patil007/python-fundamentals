#default parameter:assigning a default value to parameter , which is used when no argument
#is passed

#non-default(a) ARGUMENTS follows default arguments(b=2)


def calc_prod(a=2,b=2):
    print(a*b)
    return a*b 

calc_prod()

def calc_prod(a,b=2):
    print(a*b)
    return a*b 

calc_prod(1)


#error occure due to non -default arguments follows default arguments

# def calc_prod(a=3,b):
#     print(a*b)
#     return a*b 

# calc_prod(1)