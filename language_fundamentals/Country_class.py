'''
A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

Population is greater than 250 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object.
Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}
'''


class Country:
    def __init__(self, name_country, population, area):
        self.is_big = (population // 1000000)  > 250 or (area // 1000000) > 3
        self.name_country = name_country
        self.population = population
        self.area = area

    def compare_pd(self, country):
        str_tmp = "{} has a {} population density than {}".format(self.name_country, '{}', country.name_country)
        if self.population/self.area > country.population/country.area:
            return str_tmp.format('larger')
        return str_tmp.format('smaller')


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)
 # ➞ True
print(andorra.is_big)
 # ➞ False
print(andorra.compare_pd(australia))
 # ➞ "Andorra has a larger population density than Australia"
