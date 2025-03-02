#myDict.values() Method:Return all values

info={
    "name":"Bhagyashree",
    "subject":{
        "phy":98,
        "chem":99,
        "math":100
    }
}
print(info.values())

#typecasting:
print(list(info.values()))
print(tuple(info.values()))

#length:total number of keys

print(len(info))
print(len(tuple(info.values())))