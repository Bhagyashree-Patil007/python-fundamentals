#myDict.keys() MEthod:return all keys

info={
    "name":"Bhagyashree",
    "subject":{
        "phy":98,
        "chem":99,
        "math":100
    }
}
#not return nested keys only writen outer keys:
print(info.keys())

#typecasting:
print(list(info.keys()))
print(tuple(info.keys()))

#length:total number of keys

print(len(info))
print(len(tuple(info.keys())))
