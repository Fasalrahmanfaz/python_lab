class Emplo:
    company_name = "albaik"
    Location = "kozhikkode"
    def __init__(self,id,name,salary):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = salary
    def details(self):
        print("Company - ",self.company_name)
        print("Location - ",self.Location)
        print("Employee id - ",self.emp_id)
        print("Employee name - ",self.emp_name)
        print("Employee salary - ",self.emp_salary)
        print("\n")
emp1 = Emplo(1001,"suresh",10000)
emp2 = Emplo(1002,"remesh",25000)
emp3 = Emplo(1003,"ganesh",30000)

emp1.details()
emp2.details()
emp3.details()

