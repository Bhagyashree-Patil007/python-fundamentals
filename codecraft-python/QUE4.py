#4)wap to check entered char  is consonent or vowel using if-else statements

char=input("enter a letter: ")

if(char=='a' or char=='e'  or  char=='i' or char=='o' or  char=='u' or char=='A' or char=='E'  or  char=='I' or char=='O' or  char=='U'):
    print("vowel")
elif(char.isalpha()):
    print("consonent")
else:
    print("invalid input")

