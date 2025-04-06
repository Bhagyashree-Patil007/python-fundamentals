#19. Find longest word in list 

list=["apple","mango","orange","banana","Watermelon","Pineapple"]

longest_len=len(list[0])
longest_words="apple"

i=0
while i<len(list):
    if longest_len<len(list[i]):
        longest_len=len(list[i])
        longest_words=list[i]
    i+=1

print("longest_word:",longest_words)
print("length of longest word is:",longest_len)