#remove duplicates number from list and print the remove element from list 
list1=[1,2,3,4,5,4,33,5,1]
unique_list=[]
removed_list=[]

for num in list1:
   if num not in unique_list:
        unique_list.append(num)
   else:
       removed_list.append(num)


print("unique list elements is : ",unique_list)
print("removed elements are: ",removed_list)

 