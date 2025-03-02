#when we perform operations on write or append mode and this file not exit in system then python automatically create a these file
#1. for write mode: 
f=open("write.txt","w")# automatically create write.txt file
f.close()
#2. for append mode: # automatically create append.txt file
f=open("append.txt","a")
f.close()

f=open("C:\python\dictionary.py\demow.txt","w")
#overwrite the entire file
f.write("i want to learn something new everyday")
f.close()

