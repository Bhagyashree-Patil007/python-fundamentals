'''42) word="hello"  
vowel_Str=['a','e','i','o','u']
find vowel in word using list comprehention'''
word ="hello"
vowel_Str=['a','e','i','o','u']
for i in vowel_Str:
    for j in word:
        if j==i:
            print(j,end=' ')

