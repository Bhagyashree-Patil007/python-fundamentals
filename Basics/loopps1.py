#print number from 1 to 100:
i=1
while i<=100:
    print(i)
    i+=1

#print number from 100 to 1:
i=100
while i>=1:
    print(i)
    i-=1

#print the multiplication table of a number n:
n=int(input("enter number: "))
i=1
while i<=10:
    print(n*i)
    i+=1


#print the element of the following list using a loop:
list=[1,4,9,16,25,36,49,64,81,100]
#traverse:
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1

#search for a number x in this tuple using loop:
tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter number:"))
idx=0
while idx<len(tuple):
    if tuple[idx]==x:
        print(idx,tuple[idx])
        break
    idx+=1

#wap to find the sum of first n natural number
sum=0
n=int(input("enter number: "))
i=0
while i<=n:
    sum+=i
    i+=1
print("sum = ",sum)

#wap to find the factorial of first n natural number
fact=1
n=int(input("enter number: "))
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial = ",fact)