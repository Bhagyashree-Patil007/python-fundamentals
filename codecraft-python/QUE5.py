'''5)Implement program to input marks of three subjects and calculate its percentage, take value 
from keyboard. Display appropriate class of students based on percentage? '''
#student using if-else ladder apply all required validation.

while True:
    sub1=float(input("enter maths marks (1-100): "))

    if sub1<0 or sub1>100:
        print("enter valid marks (1-100)")
    else:
        break

while True:
    sub2=float(input("enter phy marks (between 1-100) "))
    
    if sub2<0 or sub2>100:
        print("enter valid marks (1-100):")
    else:
        break

while True:
    sub3=float(input("enter chem marks (between 1-100) "))
    
    if sub3<0 or sub3>100:
        print("enter valid marks (1-100):")
    else:
        break

Calc_per=((sub1+sub2+sub3)/300)*100

print("percentage= ",Calc_per)

if(Calc_per>=70 and Calc_per<=100):
    print("first class with distinction")

elif(Calc_per<70 and Calc_per>=60):
    print("first class ")

elif (Calc_per<60 and Calc_per>=50):
    print("second class ")

elif (Calc_per<50 and Calc_per>=40):
    print("third class ")

else:
    print("fail")



             
    
        