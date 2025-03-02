
f=open("C:\python\dictionary.py\demo.txt","r")
data=f.read()
print(data)
print(type(data))#normal output are display

#print blank (empty) line due to already all data are read only "\n" character are remaining for reading a pointer due to only blank line are printed
line1=f.readline() 
print(line1)
line2=f.readline()  
print(line2)
f.close()