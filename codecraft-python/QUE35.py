'''35. Write a Python program to check if all items in a given list of strings are equal to a given 
string. E.g.Lsit1=[“Hello”, “Hello”] & input string=”Hello” it returns True otherwise False'''
def check_all(str,list1):
    return all(item==str for item in list1)

list1=["hello","hello"]
str=input("enter string:")
print(check_all(str,list1))

