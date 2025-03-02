#TERNARY OPERATORS:

#way 1:with variable
food=input("food: ")
eat=print("yes")if food=="cake" or food== "jalebi" else print("no")
print(eat)

#way 2:without variable
food=input("food:")
print("happy")if food=="cake" or food=="jalebi" else print("very happy")

#clever if/ ternary operators:
marks=int(input("marks:"))
Grade=("fail","pass")[marks>=40]
print(Grade)

sal=float(input("salary: "))
tax=sal*(0.1,0.2)[sal>=50000]
print(int(tax))