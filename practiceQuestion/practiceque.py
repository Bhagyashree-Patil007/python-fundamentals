# f=open("practice.txt","w")
# f.write("Hi everyone \nwe are learning file i/o \nusing java \ni like programing in java")

def overwrite():
    with open("practice.txt","w") as f:
        f.write("hi everyone \nwe are learning file i/o \nusing java \ni like programing in java")

    #replaces all occurances of java with python
    with open("practice.txt","r") as f:
        data=f.read()
        new_data=data.replace("java","python")
        print(new_data)#print new data

    with open("practice.txt","w") as f:
        f.write(new_data)#overwrite update data in file

overwrite()


#search if the word "learning" exists in the file or not
print("\n--------------")
def check_for_word():
    word="learning"#exist in file
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")

    word="xlearning"#not exist in file
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):#another way: if (word in data);
            print("found")
        else:
            print("not found")

check_for_word()


#waf to find in which line of the file does the word "learning" occure first 
#print-1 if word not found
def check_for_line():
    word="python"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while True:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

    return -1

check_for_line()


