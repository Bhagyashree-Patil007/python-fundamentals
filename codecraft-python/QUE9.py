#9. WAP to display Fibonacci series up to 10 numbers? 

num1=0
num2=1
print("Fibonacci series:")
print(num1,num2,end=" ")
i=1
while i<=8:
    num3=num1+num2
    print(num3,end=" ")
    i+=1
    num1,num2=num2,num3

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.




