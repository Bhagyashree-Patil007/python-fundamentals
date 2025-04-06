#l1=[13,12,11] l2=[11,13,14] compare two list and display similar numbers from both list

l1=[13,12,11,14,19] 
l2=[11,19,13,14,15]
l3=[]
for a in l1:
    for b in l2:
        if a==b:
            l3.append(a)
    
print(l3)
