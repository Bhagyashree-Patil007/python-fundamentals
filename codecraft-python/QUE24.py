#24. WAP to swap first 2 chars of 2 strings. E.g.  'pqr', 'xyz'  o/p ‘xyr pqz’ 

str1='pqr'
str2='xyz'

new_str1=str2[:2]+str1[2]
new_str2=str1[:2]+str2[2]

print(new_str1," ",new_str2)

