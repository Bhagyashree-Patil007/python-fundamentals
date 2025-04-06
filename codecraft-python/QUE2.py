#2)wap to find  largest of 3 numbers using if-else statements?:

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))

if(num1>=num2 and num1>=num3):
    print("largest number is: ",num1)
elif(num2>=num3):
    print("largest number is: ",num2)
else:
    print("largest numbar is: ",num3)