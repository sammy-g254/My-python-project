class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary of {self.name} has been increased to {self.salary}")
    def get_annual_salary(self):
        return self.salary*12
    def change_name(self, new_name):
        self.name=new_name
        print(f"Employee name changed to {new_name}")
emp1 = employee("John", 25, 20000)
emp2 = employee("Jane", 17, 30000)
print(emp1.name)
print(emp1.age)
print(emp2.name)
print(emp2.age)
#Object.methodname
emp1.display_info()
emp1.increase_salary(15000)
print(f"The annual salary of {emp1.name} is {emp1.get_annual_salary}")
emp1.change_name("Barack")
#
class manager(employee):
    pass
mg1=manager("Jacob",29,90000)
print(mg1.name)
mg1.display_info()