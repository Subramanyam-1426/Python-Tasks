class employee:
    # Stores the total number of employees.
    total_employee = 0

    # Stores the company name shared by all employees.
    company_name = "TechCorp Solutions"

    # Stores the PF contribution percentage.
    pf_percentage = 12.0

    # Defines the minimum allowed salary.
    MIN_Salary = 15000

    # Defines the maximum allowed salary.
    MAX_Salary = 500000

    # Stores the next PAN number to be assigned.
    last_pan_number = 1001

    # Initializes a new employee with personal and salary details.
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self._emp_id = emp_id
        self._department = department
        self._salary = 0
        self.dmsalary = salary
        self.varun = 0
        employee.total_employee += 1
        self.__pan_number = employee.last_pan_number
        employee.last_pan_number += 1

    # Returns the employee ID.
    @property
    def emp_id(self):
        return self._emp_id

    # Returns the employee's current salary.
    @property
    def dmsalary(self):
        return self._salary

    # Validates and sets the employee's salary.
    @dmsalary.setter
    def dmsalary(self, value):
        if (not isinstance(value, (int, float))):
            raise TypeError
        if value < employee.MIN_Salary or value > employee.MAX_Salary:
            raise ValueError(
                f"Salary must be between {employee.MIN_Salary} and {employee.MAX_Salary}")
        self._salary = value

    # Applies a salary hike and returns the updated salary.
    def apply_hike(self, percent):
        if percent < 0 or percent > 50:
            raise ValueError(f"hike percent must be in 0 to 50 ")
        ns = (0.01 * percent) * self.dmsalary + self.dmsalary
        self.dmsalary = ns
        return self.dmsalary

    # Calculates and returns the employee's PF amount.
    def calculate_pf(self):
        return (self.dmsalary * employee.pf_percentage) / 100

    # Returns the total number of employees created.
    @classmethod
    def get_total_employee(cls):
        return cls.total_employee

    # Transfers the employee to a new department.
    def transfer_department(self, new_dept):
        dm = self._department
        self._department = new_dept
        return f"employee [{self.name}] transfers from {dm} department to {new_dept} departmenent"

    # Checks whether the given salary is valid.
    @staticmethod
    def is_valid_salary(value):
        if (not isinstance(value, (int, float))):
            raise TypeError
        if value < employee.MIN_Salary or value > employee.MAX_Salary:
            return False
        return True

    # Displays the employee details.
    def prints(self):
        print(f"Employee {self._emp_id} {self.name} | {self._department} | {self._salary} ")


# Demonstrates employee creation and various employee operations.
def main():

    try:
        print(f"Company: {employee.company_name}")
        print(f"Employees before: {employee.total_employee}")

        E1 = employee("Subramanyam", "101", "engineering", 400000)
        E2 = employee("Aravind", "101", "engineering", 450000)

        E1.prints()
        E2.prints()

        print(f"Employees after: {employee.total_employee} ")
        print(f"PF for el : {E1.calculate_pf()}")
        print(f"After 10% hike: {E1.apply_hike(10)}")
        print(E1.transfer_department("LLM engineering"))
        print(f"is_valid_salary(9000): {employee.is_valid_salary(9000)}")

    except (TypeError, ValueError) as err:
        print(err)

    try:
        E3 = employee("Ramesh", "103", "engineering", 9000)
    except (TypeError, ValueError) as err:
        print(f"Blocked : {err}")

    try:
        E1.emp_id = 103
    except (AttributeError) as err:
        print(f"Blocked : {err}")

    print(f"protected : {E1._department}")
    print("Private : ", E1._employee__pan_number)


# Executes the program when this file is run directly.
if __name__ == "__main__":
    main()