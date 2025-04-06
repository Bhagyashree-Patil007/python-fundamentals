#14. WAP to check number is Armstrong or not using function?

def Armstrong(num):
    num=str(num)
    n=len(num)

    #Using loop:
    add=0
    for digit in num:
        add+=int(digit)**n

    #using list comprehention:using sum function
    # add=sum(int(digit)**n for digit in num)

    num=int(num)
    if add==num:
        print("Armstrong")
    else:
        print("Non Armstrong")

# Armstrong numbers examples :153,370,371,407,54748,8208
# non Armstrong numbers examples : 123,200,9475,99
Armstrong(153)


