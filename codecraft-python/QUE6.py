#6. WAP to find factorial of given number using while loop? 
while True:
    num=int(input("enter the number for factorial :"))
    if num<0:
        print("negative numbers do not have a factorial!...")
        print("Enter Positive Number...")
    else:
        break

fact=1
i=1
while i<=num:
    fact=fact*i   
    i=i+1
print("factorial : ",fact) 