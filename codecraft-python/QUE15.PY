#15. WAP to find Armstrong number using lambda function? 

num=int(input("enter number: "))
num_str=str(num)
n=len(num_str)

arm=lambda:sum(int(digit)**n for digit in num_str)
print("Armstrong" if int(num_str)==arm() else "non Armstrong")

