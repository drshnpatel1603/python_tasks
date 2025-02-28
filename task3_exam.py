# Task 3: Employee Management System with Class-Level Storage using List of Dictionaries

class Employee:
    employees = [{'employee_id': 1001, 'name': 'Darshan', 'salary': 5000, 'role': 'Devloper', 'extra_info': 'Python'}, {'employee_id': 1002, 'name': 'Dhruv', 'salary': 10000, 'role': 'Devloper', 'extra_info': 'Java'}]

    def add_empolyee(self):
        # unique id assign
        if len(self.employees) == 0:
            self.id = 1001
        else:
            self.id = len(self.employees) + 1001

        # input - employee value
        self.employee_id = self.id
        self.name = input("Enter Empolyee Name : ").capitalize()
        self.salary = int(input("Enter Empolyee Salary : "))
        self.role = input("Enter Empolyee role : ").capitalize()
        self.extra_info = input("Enter Extra Information of Empolyee: ").capitalize()
        try:
            self.employees.append({"employee_id":self.employee_id, "name" : self.name, "salary" : self.salary, "role" : self.role, "extra_info" : self.extra_info})
            print("Data Successfully Enterd!")
        except Exception as e:
            print(e)

    def display_all_employees(self):
        # Print Employees Data
        for data in self.employees:
            print(data)

    def filter_by_role(self,role):
        # Filter Data by role base
        self.flag = True
        for data in self.employees:
                if data.get("role") == role:
                    print(data)
                    self.flag = False
        if self.flag:
            print(f"Data not Found for {role}")

    def filter_by_salary(self,min_salary, max_salary):
        # Filter Data by salary Base
        self.flag = True
        for data in self.employees:
            if data.get("salary") >= min_salary and data.get("salary") <= max_salary:
                print(data)
                self.flag = False
        if self.flag:
            print(f"Data not Found between {min_salary} to {max_salary} salary")

# createing object of emyployees class
e1 = Employee()
while(True):
    try:
        print()
        print("1. Add Employee ")
        print("2. Display Employees List ")
        print("3. Employee filter by role  ")
        print("4. Filter employees by salary range ")
        print("5. Exit")

        user = int(input("Select An options : "))
        match(user):
            case 1:
                e1.add_empolyee()
            case 2:
                e1.display_all_employees()
            case 3:
                role = input("Enter the Role Manager or Developer:").capitalize()
                e1.filter_by_role(role=role)
            case 4:
                min_salary = int(input("Enter the Minimum Salary :"))
                max_salary = int(input("Enter the Maximum Salary :"))
                e1.filter_by_salary(min_salary=min_salary,max_salary=max_salary)
            case 5 :
                break
    except Exception as e:
        print(e)

