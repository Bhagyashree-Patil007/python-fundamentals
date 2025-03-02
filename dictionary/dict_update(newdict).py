#myDict.update(newdict) MEthod: insert the specified items to the dictionary

info={
    "name":"Bhagyashree",
    "subject":{
        "phy":98,
        "chem":99,
        "math":100
    }
}

#way1:add new key value pair

info.update({"city":"delhi"})
print(info)

#way2:add new key value pair //key value is also updated for same kay name(overwrite)for old kay name
new_dect={"rollno":39,"age":18,"name":"Vinay"}
info.update(new_dect)
print(info)
