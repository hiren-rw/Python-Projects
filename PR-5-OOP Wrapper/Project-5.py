""" Project-5 : OOP Wrapper """
# Employee Management System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

    def __del__(self):
        # Destructor to clean up resources
        pass


class Employee(Person):
    # Method Overloading Simulation using default arguments
    def __init__(self, name, age, emp_id=None, salary=0.0):
        super().__init__(name, age)
        # Encapsulation: Making sensitive data private
        self.__emp_id = emp_id
        self.__salary = float(salary)

    # Getter and Setter for Employee ID
    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter and Setter for Salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = float(salary)

    # Method Overriding
    def display(self):
        super().display()  # Call parent class display
        print(f"Employee ID: {self.get_emp_id()}")
        print(f"Salary: ${self.get_salary():.1f}")

    def __del__(self):
        # Destructor message when object resources are freed
        pass


class Manager(Employee):        # Multilevel Inheritance
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):      # Hybrid Inheritance
    def __init__(self, name, age, emp_id, salary, programming_language):
        super().__init__(name, age, emp_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


def main():
    # Lists to store created objects
    database = {"Person": [], "Employee": [], "Manager": [], "Developer": []}

    print("--- Python OOP Project: Employee Management System ---")

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                name = input("\nEnter Name: ")
                age = int(input("Enter Age: "))

                person = Person(name, age)
                database["Person"].append(person)

                print(f"\nPerson created with name: {name} and age: {age}.")

            case 2:
                name = input("\nEnter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))

                emp = Employee(name, age, emp_id, salary)
                database["Employee"].append(emp)

                print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary:.1f}.")

            case 3:
                name = input("\nEnter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                dept = input("Enter Department: ")

                manager = Manager(name, age, emp_id, salary, dept)
                database["Manager"].append(manager)

                print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary:.1f}, and department: {dept}.")

            case 4:
                name = input("\nEnter Name: ")
                age = int(input("Enter Age: "))
                dev_id = input("Enter Developer ID: ")
                salary = float(input("Enter Salary: "))
                programming_lang = input("Enter Programming Language: ")

                developer = Developer(name, age, dev_id, salary, programming_lang)
                database["Developer"].append(developer)

                print(f"\nDeveloper created with name: {name}, age: {age}, ID: {dev_id}, salary: ${salary:.1f}, and programming language: {programming_lang}.")

            case 5:
                print("\nChoose details to show:")
                print("1. Person")
                print("2. Employee")
                print("3. Manager")
                print("4. Developer")

                try:
                    sub_choice = int(input("\nEnter your choice: "))
                    category_mapping = {
                        1: "Person",
                        2: "Employee",
                        3: "Manager",
                        4: "Developer",
                    }
                    category = category_mapping.get(sub_choice)

                    if category:
                        # Demonstrate the use of issubclass() as required
                        class_objects = {
                            "Person": Person,
                            "Employee": Employee,
                            "Manager": Manager,
                            "Developer": Developer,
                        }
                        target_class = class_objects[category]

                        if target_class != Person and issubclass(target_class, Employee):
                            print(
                                f"\n[System Info: Verified that {category} is a subclass of Employee]"
                            )

                        records = database[category]
                        if not records:
                            print(f"\nNo records found for {category}.")
                        else:
                            for idx, obj in enumerate(records, 1):
                                print(f"\n{category} Details:")
                                obj.display()
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input.")

            case 6:
                # Clear references to simulate resource cleanup and invoke destructors
                database.clear()
                print("\nExiting the system. All resources have been freed.")
                print("\nGoodbye!")
                break
            case _:
                print("Invalid choice. Please select between 1 and 6.")

        print("\n--- Choose another operation ---")

main()