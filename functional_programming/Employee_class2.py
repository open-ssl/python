'''
Create a class Employee that will take a full name as argument,
as well as a set of none, one or more keywords.
Each instance should have a name and a lastname attributes
plus one more attribute for each of the keywords, if any.
'''


class Employee:
    def __init__(self, name, salary=None, height=None, nationality=None, subordinates=None):
        self.name, self.lastname = name.split()
        self.salary = salary
        self.height = height
        self.nationality = nationality
        self.subordinates = subordinates



john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
