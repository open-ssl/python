'''Write a Composer class that has three instance variables:

name
dob
country
Add an additional class variable .count which counts the total number of instances created.

'''


class Composer():
    count = 0
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1

print(Composer.count)
# Composer.count

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
# print(Composer.count)

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
# print(Composer.count)
