class Employee:
    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def Employee_detail(self):
        print("Name of employee:",self.name)
        print("Employee id:",self.empid)
        print("Salary of employee:",self.salary)


e1 = Employee(20489,"Ayush","100000 USD")
e1.Employee_detail()