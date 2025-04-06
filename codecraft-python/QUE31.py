'''31. Write a Python program to count the number of strings from a given list of strings. The string 
length is 2 or more and the first and last characters are the same'''
list = ["radar","banana","Watermelon", "deed","apple","mango","orange","civic", "deed", "noon","banana","Watermelon"]
list1=[]

count=0
for i in list:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
        list1.append(i)

print(list1)
print("the count of string is:",count)
