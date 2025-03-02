
#list:
list=[1,2,3,4,4]
for i in list:
    print(i,end=" ")

print("\n")

#tuple:
fruits=("apple","banana","orange")
for i in fruits:
    print(i,end=" ")

print("\n")

#string:
str="Bhagyashree"
for i in str:
    print(i,end=" ")
else:#print hoga loop stop hone ke bad
    print("\nend")

lists=[1,4,9,16,25,36,49,64,81,100]
print("\n")
for i in lists:
    print(i,end=" ")

print("\n")

tuple=(1,4,9,16,25,36,49,64,25,81,100)
n=int(input("enter no: "))
idx=0
for j in tuple:
    if j==n:
        print("num found at idx",n,idx)        
    idx+=1
    

#wap to find the sum of first n natural number    
sum=0
n=int(input("enter number: "))
for i in range(1,n+1):
    sum+=i
print("total sum = ",sum)

#wap to find the factorial of first n natural number
fact=1
n=int(input("enter number: "))
for i in range(1,n+1):
    fact*=i
print("factorial = ",fact)
    
    

