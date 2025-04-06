#10. Implement program to count total even/odd number from the array? 

import array
arr=array.array('i',[1,2,3,4,5,6,7,8,9,10])

count=0
print("Even Numbars are:")
for e in arr:
    if e%2==0:
        print(e,end=" ")
        count+=1
print("\nThe total count of even numbers are:",count)

print("\n------------")
count=0
print("Odd Numbars are:")
for e in arr:
    if e%2!=0:
        print(e,end=" ")
        count+=1
print("\nThe total count of even numbers are:",count)


