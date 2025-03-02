
#function definition:
def calc_Sum(a,b):
    print(a+b)
    return a+b

def print_Hello():
    print("hello")

def ave__Of_No(a,b,c):
    print((a+b+c)/3)

#function call:
print(calc_Sum(3,4))#7
calc_Sum(4,4)
calc_Sum(10,4)
print_Hello()
print_Hello()
print_Hello()
#when the function which does not return any value or anything
#the the output automatically converted into NONE value
output=print_Hello()
print(output)#NONE

print(ave__Of_No(2,3,4))#none
ave__Of_No(2,3,8)