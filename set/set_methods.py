#set.add(el):adds an element

college=set()
print(college)
college.add(1)
college.add(2)
college.add(3)
#ignore duplicate value:
college.add(2)
college.add("Patil")
college.add((4,5,6))
#we can not pass list and dict:due to they are mutable//erroe occur
#college.add([9,3,4])
# college.add({"name":"Bhagu"})
print(college)

#set.remove(el):remove the element

set=set()
print(set)
set.add(1)
set.add(2)
set.add(3)
set.add(4)
print(set)
#remove element:
set.remove(3)
#value not exist in set:error occured
#set.remove(9)
print(set)

#set.clear():empties the element
set1={1,2,3,4}
print(len(set1))
set1.clear()
print(len(set1))

#set.pop():remove a random value
set2={"hi","hello","hey"}
print(set2.pop())
print(set2)

#set.union(set2):combines both set values & returns new
set1={1,2,3}
set2={3,2,5}
#make a new set
print(set1.union(set2)) #{1,2,3,5}

#not change in original set
print(set1)
print(set2)

#set.intersection(set2):combines common values & returns new
set4={1,2,3}
set5={3,2,5}
#make a new set
print(set4.intersection(set5)) #{2,3}

#not change in original set
print(set4)
print(set5)
