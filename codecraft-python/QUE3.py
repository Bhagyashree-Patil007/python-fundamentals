#3)wap that reads a value from keyboard and check +ve or -ve
while True:
    num=input("enter a number:  ")
    if num=="quit":
        break
    if num.lstrip('-') .isdigit() :
        num=int(num)
        if(num>0):
            print("number is positive")
        elif(num<0):
            print("number is negative")
        elif(num==0):
            print("number is zero")
    else:
        print("invalid input")


# num=int(input("enter a number:  "))
# if(num>0):
#     print("number is positive")
# elif(num<0):
#     print("number is negative")
# elif(num==0):
#     print("number is zero")





