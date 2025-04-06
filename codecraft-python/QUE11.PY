#11. Implement program to find total occurrences of given number from the array? 

#Mannually:
import array
arr=array.array('i',[1,2,3,4,5,6,7,8,9,10,1,2,2,2,3])
Num=int(input("Enter the number"))
count=0
for i in arr:
    if i==Num:
        #print(i)
        count+=1

print("total occurrences of",Num,"is:",count)

#using Built-in function:
num1=arr.count(Num)
print("total occurrences of",Num,"is:",num1)

