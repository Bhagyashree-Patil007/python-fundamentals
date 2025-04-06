#20. WAP to reverse the word in given string

Str="Hello DYPCET"
print(Str[::-1])
words=Str.split()


reversed_word=" ".join(word[::-1]  for word in words)

print(reversed_word)