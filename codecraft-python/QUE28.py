#28. Remove duplicate numbers from list
random_numbers = [3, 7, 2, 9, 3, 5, 7, 1, 4, 2, 8, 6, 9, 5, 4, 3, 8, 6, 1, 7]
unique_no=[]
duplicate_no=[]

for num in random_numbers:
    if num not in unique_no:
        unique_no.append(num)
    else:
        duplicate_no.append(num)

print(unique_no)
print(duplicate_no)