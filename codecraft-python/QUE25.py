#25. WAP to reverse string if length is a multiple of 4 
list=["apple","mango","orange","banana","Watermelon","Pineapple","Kiwi","Plum","Pear","Date"]
for i in list:
    if len(i)%4==0:
        #i=i[::-1]
        #print(i,end=' ')
        reversed_fruit=""
        for char in i:
            reversed_fruit=char+reversed_fruit
        print(reversed_fruit,end=" ")
        

