# WAP to make a employee class where method are calculated_bonus,
# calculate_total_salary.
#initi method takes as argument as name, toatal_salary,age,post, annd t and bonus
#and bonus_percentage.# calculate_bonus function are used to calculate total bonus in flat,
# total salary of bonus_persentage and calculate_total_salary function are used
# to calculate total salary recived with including bonus given by company

class Employee:
    def __init__(self, name, normal_salary, age, post, bonus_percentage):
        self.name = name
        self.normal_salary = normal_salary
        self.age = age
        self.post = post
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self):
        return (self.normal_salary * self.bonus_percentage) / 100
    
    def calculate_total_salary(self):
        return self.normal_salary + self.calculate_bonus()


employees = []

n = int(input("How many employees do you want to enter? "))

for i in range(n):
    print(f"\nEnter details of Employee {i+1}:")
    name = input("Name: ")
    normal_salary = float(input("Normal Salary: "))
    age = int(input("Age: "))
    post = input("Post: ")
    bonus_percentage = float(input("Bonus Percentage: "))
    
    emp = Employee(name, normal_salary, age, post, bonus_percentage)
    employees.append(emp)


print("\n -- Employee Details --")
for emp in employees:
    print("-----------")
    print(f"Employee: {emp.name}")
    print(f"Post: {emp.post}")
    print(f"Normal Salary: {emp.normal_salary}")
    print(f"Bonus: {emp.calculate_bonus()}")
    print(f"Total Salary (with Bonus): {emp.calculate_total_salary()}")
