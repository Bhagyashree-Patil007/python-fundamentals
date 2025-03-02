
f=open("C:\python\dictionary.py\demo.txt","r")

line1=f.readline() 
print(line1)#blank line are printed due to "\n"

line2=f.readline()  
print(line2)

#print empty line:due to don't have any more data in the file
line2=f.readline()  
print(line2)
f.close()