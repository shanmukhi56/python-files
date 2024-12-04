class Employee:
    def __init__(self, name, employee_id, salary):
        """
        Initialize the employee with name, ID, and salary.
        """
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """
        Display the employee's details including name, ID, and salary.
        """
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary:.2f}")

    def give_raise(self, percent):
        """
        Increase the salary by the given percentage.
        """
        if percent > 0:
            raise_amount = self.salary * (percent / 100)
            self.salary += raise_amount
            print(f"Salary increased by {percent}% ({raise_amount:.2f}). New salary: ₹{self.salary:.2f}")
        else:
            print("Raise percentage must be positive.")

# Example Usage
# Create an employee
employee = Employee("Alice Johnson", "E12345", 50000)

# Display initial details
employee.display_details()

# Give a raise of 10%
employee.give_raise(10)

# Display updated details
employee.display_details()
