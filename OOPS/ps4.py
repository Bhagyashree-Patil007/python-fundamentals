class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def ShowDetails(self):
        print("employee role: ",self.role)
        print("employee dept: ",self.dept)
        print("employee salary: ",self.salary)


class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age

        print("employee name: ",self.name)
        print("employee age: ",self.age)
        super().__init__("engineer","Al","1,00,000")

e1=Engineer("vinay",21)
e1.ShowDetails()
