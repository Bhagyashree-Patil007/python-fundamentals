#17. WAP to identify only integer numbers from the list of mixed elements using filter function?

def int_num(list1):
    return type(list1)==int
    
list1=["apple","hi",True,1.90,1,2,3]

integer_num=filter(int_num,list1)
print(list(integer_num))

