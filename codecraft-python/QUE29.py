#29. Write a Python program to count the number of elements in a list within a specified range.

random_numbers = [3, 7, 2, 9, 3, 5, 7, 1, 4, 2, 8, 6, 9, 5, 4, 3, 8, 6, 1, 7]
count=0
list=[]
for i in random_numbers:
    if i>2 and i<6:
        list.append(i)
        count+=1

print(list)
print(count)

