#from a file containing numbers separated by comma, print the count of even numbers
#1.without in-built function:
# with open("countno.txt","r") as f:
#     data=f.read()
#     print(data)

#     count=0
#     num=""
#     for i in range(len(data)):
#         if data[i]==",":
#             if (int(num)%2==0):
#                 print(int(num))
#                 count+=1
#             num=""
#         else:
#             num+=data[i]
#     print()
# print(count)

#2.with in-built function:

count=0
with open("countno.txt","r") as f:
    data=f.read()
    print(data)
    nums=data.split(",")#create nums list
    print(nums)
    for val in nums:
        if val:
            if (int(val)%2==0):
                count+=1

print(count)