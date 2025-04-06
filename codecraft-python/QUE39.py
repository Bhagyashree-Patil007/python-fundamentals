#39)display elements from list having length equal to 4 using list
list=["apple","mango","orange","banana","Watermelon","Pineapple","Kiwi","Plum","Pear","Date"]
list1=[]
for i in list:
    if len(i)==4:
        list1.append(i)

print(list1)

