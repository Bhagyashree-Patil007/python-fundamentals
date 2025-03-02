num=int(input("enter number:"))

if num==0:
    print("zero")
elif num<0:
    print("invalid input") 
    print("plz enter valid input")
elif num%2==0:
    print("even")
else:
    print("odd")
