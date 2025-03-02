with open("C:\python\dictionary.py\with.txt","r") as f:
    data=f.read()
    print(data)#print data within file

with open("C:\python\dictionary.py\with.txt","w") as f:
    f.write("new data")  # trancate file and store new data in file