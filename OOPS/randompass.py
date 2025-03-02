#GENERATE RANDOM PASSWORD:

#1.
import random
import string 
pass_len=8

charValues=string.ascii_letters+string.punctuation+string.digits

password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("random password is: ",password)

2.
import random
import string 
pass_len=8

password="".join(random.choices(string.ascii_letters+string.punctuation+string.digits,k=9))
print("random password is: ",password)

#3.
import random
import string 
pass_len=8

charValues=string.ascii_letters+string.punctuation+string.digits

#list comprehention [function for i in range(n)]
password="".join([random.choice(charValues)for i in range(pass_len)])

print("random password is: ",password)

