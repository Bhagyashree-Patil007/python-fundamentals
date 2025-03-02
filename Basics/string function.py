#string function:

str="i am very happy"

# 1) .endswith(""); two possibilities a)true b)false
print(str.endswith("ppy"))
print(str.endswith("ly"))

# 2) .capitalize("");two possibilities 
                    #a)temporary changed  b)parmanantely changed

#a)
print(str.capitalize())
print(str)

#b)
str=str.capitalize()
print(str)

# 3) .replace("old","new");1)single letter(ex..,'e''w')  2)string(ex..,"from")
print(str.replace("p","qq"))
print(str.replace("very","extremely"))

# 4) .find(): 1)single letter(ex.,'e')  2)string (ex.,"very") 3)non-existing string or character:
print(str.find('a'))
print(str.find("very"))
print(str.find("patil"))

# 5) .count(): 1)single letter(ex.,'e')  2)string(ex.,"very")  3)absent string
print(str.count('a'))
print(str.count("very"))
print(str.count('z'))
