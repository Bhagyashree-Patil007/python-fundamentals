'''16. WAP to check numbers even or odd from list and perform square of each even number using
map function?'''

p=[1,2,3,4,5,6,7,8,9,10]
i=p[0]
while i<=len(p):
    result=lambda i: "even" if i%2==0 else "odd"
    print(i,result(i),end=" ")
    result=map(lambda y:y*y,[i])
    print(list(result))
    i+=1
