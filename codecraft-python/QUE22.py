#22. Given string s1='abc' and s2='pqr' change alternate word of string e.g apbqcr 

#daut:how to exicute program when string length are diff
s1="abc"
s2="pqr"

result=[]
for i in range(len(s1)):
    result+=s1[i]+s2[i]
   

print(''.join(result))                                                                                                               