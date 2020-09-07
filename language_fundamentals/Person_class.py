'''
Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
'''


class Person:
    def __init__(self, name, lst_good, lst_bad):
        self.name = name
        self.lst_good = lst_good
        self.lst_bad = lst_bad

    def taste(self, txt):
        return_txt = '{} eats the {}'.format(self.name, txt)
        if txt in self.lst_good:
            return_txt += " and loves it"
        elif txt in self.lst_bad:
            return_txt += " and hates it"
        return return_txt + '!'


p1 = Person("Sam", ["ice cream"], ["carrots"])

print(p1.taste("ice cream"))
 # ➞ "Sam eats the ice cream and loves it!"

print(p1.taste("cheese"))
 # ➞ "Sam eats the cheese!"

print(p1.taste("carrots"))
 # ➞ "Sam eats the carrots and hates it!"
