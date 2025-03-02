
info={
    "key":"value",
    "name":"Bhagyashree",
    "rollno":37,
    "dept":"DS",
    "topics":("dict","set"),
    "subject":["python","c"],
    #keys may be number(int or float),boolean,tuple due to they are immutable
    #but dictinary and list they are mutable so it is not use for key
    #keys are immutable
    12.99:12,
    True:1,
    (1,2):17

}
print(info)
print(type(info))

#accessing  values with the help of keys:
print(info["name"])
print(info["subject"])
print(info["topics"])
print(info[True])

#when we try to print value which is not present then error are occure
# print(info["surname"])

#change values with the help of keys:
info["name"]="Dyp"
print(info["name"])

#we can also add new key:value pair:
info["surname"]="Patil"
print(info["surname"])

#we can not create same key name again beacause the old value are overwrite

#we can also create null dictionary:
null_dict={}
#we can also add values
null_dict["name"]="Google"
print(null_dict)