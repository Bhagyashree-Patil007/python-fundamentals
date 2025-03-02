#myDict.items() MEthod:return all (kay,val) pairs as tuple

info={
    "name":"Bhagyashree",
    "subject":{
        "phy":98,
        "chem":99,
        "math":100
    }
}
#not return nested keys only writen outer keys:
print(info.items())

#typecasting:
print(list(info.items()))

#accesing individual pair:
pairs=list(info.items())
print(pairs[0])
print(pairs[1])

#length:total number of keys

print(len(info))
print(len(tuple(info.items())))
