class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def calculate_salary(self):
        return self.base_salary

    def __str__(self):
        return f"{self.name} {self.base_salary}"

class Manager(Employee):
    def __init__(self,name,base_salary,bonus):
        super().__init__(name, base_salary)
        self.bonus=bonus
    def calculate_salary(self):
        return self.base_salary + self.bonus

class Developer(Employee):
  def __init__(self, name, base_salary, project_allowance):
        super().__init__(name, base_salary)
        self.project_allowance=project_allowance
  def calculate_salary(self):
        return self.base_salary + self.project_allowance

Employee=[
    Manager('lena',20,500),
    Developer('alice',400,300),
    Employee('minnu',600)
]

for emp in Employee:
    salary=emp.calculate_salary()
    print(f"{emp} ${salary:,.2f}")