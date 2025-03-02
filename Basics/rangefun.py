seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

print("\n")
for i in seq:
    print(i,end=" ")

print("\n")
for i in range(5):
    print(i,end=" ")

#even number:
print("\n")
for i in range(2,102,2):
    print(i,end=" ")

#print number 1 to 100:
print("\n")
for i in range(100,0,-1):
    print(i,end=" ")

#print the multiplication table of number n:
print("\n")
n=int(input("enter number"))
for i in range(1,11,1):
    print(i*n,end=" ")