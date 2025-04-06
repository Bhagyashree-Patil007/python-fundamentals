#38 display square of odd numbers between 1 to 20 using list comprehention

num=[i*i for i in range(1,21) if i%2!=0]
print(num)