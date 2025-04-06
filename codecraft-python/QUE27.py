'''27. Write a Python program to find the list of words that are longer than n from a given list of 
words. '''
random_words =["apple", "noon", "civic", "deed","Bhagyashree","Aishwarya"]
count=0
list1=[]
n=int(input("enter number for search length: "))
for i in random_words:
    if len(i)>n:
        count+=1
        list1.append(i)
        
print(list1)
print("the count of string are:",count)


