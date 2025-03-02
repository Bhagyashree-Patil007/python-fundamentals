dict={
    "table":["a piece of furniture"," list of facts and figures"],
    "cat":"a small animal"
}
print(dict)

#count of unique values:
classroom={"java","python","c++","python","javascript","java","python","java","c++","c"}
print(len(classroom))

marks={}

phy=int(input("enter marks;"))
marks.update({"phy":phy})

chem=int(input("enter marks;"))
marks.update({"chem":chem})

maths=int(input("enter marks;"))
marks.update({"maths":maths})

print(marks)

#store same values in tuple  using built-in data type
set={9,"9.0"}
print(set)

values={
    ("float",9.0),
    ("int",9)
}
print(values)