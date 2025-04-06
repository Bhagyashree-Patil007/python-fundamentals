#32. WAP to remove Even Numbers from List

numbers = [121, 3443, 78987, 123, 44, 1001, 56, 67876, 98089, 777, 909, 23]
odd_numbers=[]

for i in numbers:
    if i%2!=0:
        odd_numbers.append(i)

print("List after removing even numbers:", odd_numbers)