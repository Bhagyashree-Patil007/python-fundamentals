#30. print number in sorted order without inbuilt function 
random_numbers = [3, 7, 2, 9, 3, 5, 7, 1, 4, 2, 8, 6, 9, 5, 4, 3, 8, 1, 7]

for i in range(len(random_numbers)):
    for j in range(len(random_numbers)):
        if random_numbers[j]>random_numbers[i]:
            random_numbers[i],random_numbers[j]=random_numbers[j],random_numbers[i]


print(random_numbers)