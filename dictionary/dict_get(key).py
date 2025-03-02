#myDict.get("key") MEthod:return the key according to value

info={
    "name":"Bhagyashree",
    "subject":{
        "phy":98,
        "chem":99,
        "math":100
    }
}


print(info.get("name")) #when we return wrong key name they they return NONE value

print(info["name"])#when we return wrong key name they they return ERROR
#after these statement code are not run show error 