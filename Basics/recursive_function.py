def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
    print("end")
show(5)


#factorial:
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

print(fact(5))

#write a recursive function to calculate the sum of first n natural numbers
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

print(sum(10))

#write a ricursive function to print all elements in a list(use list & index as parameter)
def print_list(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
lang=["c","c++","python","java"]

print_list(lang)