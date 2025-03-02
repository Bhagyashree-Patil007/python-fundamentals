f=open("C:\python\dictionary.py\demo.txt","r")
data=f.read()
print(data)
print(type(data))

# #passing arguments for reading data that you want
data1=f.read(5)
print(data1)


#read one lines at a time
line1=f.readline() #read a character which is "\n" at end of each line
 #take extra space which is \n to print next blank line
print(line1)
#print  blank line
line2=f.readline()  
print(line2)
f.close()