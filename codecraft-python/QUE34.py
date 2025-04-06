#34. WAP to take two lists and find common elements in the list.
list1=["apple", "banana","mango", "orange", "peach", "pear"]
list2=["banana", "cherry", "kiwi", "fig", "apple", "grape", "melon", "peach", "plum", "papaya"]
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)

print("common elements are:",list3)
