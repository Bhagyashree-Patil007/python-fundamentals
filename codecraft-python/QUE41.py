'''temp=[1,4,3,5,2,6,7]
show thw pairs where sum=8
'''
temp=[1,4,3,5,2,6,7]
for i in range(len(temp)):
   for j in range(i+1,len(temp)):
      if temp[i]+temp[j]==8:
         print(temp[i],temp[j])
