#8. WAP to count even and odd number between 1 to 20. 
count=0
for i in range(1,21):
    if(i%2==0):
        print(i,end=" ")
        count=count+1
print("\ntotal count of even numbers are: ",count)

print("\n----------")
count=0
for i in range(1,21):
    if(i%2!=0):
        print(i,end=" ")
        count=count+1
print("\ntotal count of odd numbers are: ",count)