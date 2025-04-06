#21. WAP to find palindrome string without slicing

str=input("enter string: ")
is_palindrome=True
i=0
j=len(str)-1
while i<len(str):
    if str[i]!= str[j]:
        is_palindrome=False
        break
    i+=1
    j-=1

if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")
    

