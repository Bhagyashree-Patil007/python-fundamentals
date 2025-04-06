#12. WAP to find largest no from the array?

import array
arr=array.array('i',[1,2,3,4,5,6,7,8,9,100,1,2,2,2,434])

index=0
largest=arr[0]
for i in range(1,len(arr)):
    if largest<arr[i]:
        largest=arr[i]
        index=i
        
        
print("Largest number index is: ",index)
print("Largest number is: ",largest)