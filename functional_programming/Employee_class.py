'''
In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes
and assigns them to the correct properties. Properties will be separated by a dash.
'''


class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def from_string(str_parsing):
        firstname, lastname, salary = str_parsing.split('-')
        return Employee(firstname, lastname, int(salary))


'''
emp1.firstname ➞ "Mary"

emp1.salary ➞ 60000

emp2.firstname ➞ "John"

emp2.salary ➞ 55000
'''


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")


print(emp1.salary)
print(emp2.salary)
