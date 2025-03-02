import random
randomNum=random.randint(1,5) #print the random integer between the given range(1 & 5 are included )
print(randomNum)

import string
letter=string.ascii_letters  #print lower and uppercase letter
print(letter)
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789
print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# String Formatting with string Module
#Template Class
#1.
from string import Template

template = Template("Hello, my name is $name and I am $age years old.")
result = template.safe_substitute(name="Alice", age=25)

print(result)  # Output: Hello, my name is Alice and I am 25 years old.

#2.
import string

class CustomTemplate(string.Template):
    delimiter = "@"

template = CustomTemplate("Hello, my name is @name and I am @age years old.")
result = template.substitute(name="David", age=40)

print(result)

#3.
data = {"name": "Charlie", "age": 30}
template = Template("Hi $name, you are $age years old.")
result = template.substitute(data)

print(result)  # Output: Hi Charlie, you are 30 years old.



#Checking Character Types
import string

text = "Hello123!"
#1.
letters_only = "".join(c for c in text if c in string.ascii_letters)
digits_only = "".join(c for c in text if c in string.digits)
print(letters_only)  # Hello
print(digits_only)   # 123
#2.
letters_only = "".join(filter(lambda c: c in string.ascii_letters, text))
digits_only = "".join(filter(lambda c: c in string.digits, text))

print(letters_only)  # Output: Hello
print(digits_only)   # Output: 123



#Generating Random Strings
import random
import string

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(random_string)  # Random alphanumeric string of length 10

