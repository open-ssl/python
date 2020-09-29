
str1 = " My new endless Stroke "

# print(str1.strip())


# print(str1.lower())

# print(str1.upper())

# print(str1.replace('e', 'eeee'))

# print(str1.split())
# print(type(str1.split()))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# print('stasstas')

str2 = 'another stroke'
# print(str2.capitalize())

str3 = 'AAA'

# twice
# print(str3.casefold())
# print(str3.lower())



# print(str3.center(20))
# print(str3.count('a'))
# print(str3.count('A'))

# print(str3.encode()[0])

# print(str3.endswith('A'))
# print(str3.expandtabs(0))


# print(str3.find('B')) # -1
# print(str3.find('A'))
# print(str2.find('t'))

# twice, but find is better
# print(str3.find('B')) # -1
# print(str3.index('n')) # if not found will ValueError

str4 = '4142141  '

# isalnum -- meaning alphabet letter (a-z) and numbers (0-9).
# print(str3.isalnum())
# print(str4.isalnum())

str5 = '12'

# decimal is all (0-9) numbers
# print(str3.isdecimal())
# print(str5.isdecimal())

# print(str5.isdigit())


str6 = '''strsassaAAAAsdsds adfasad adadasd'''

# digits (0-9) letters (a-Z) and _
# print(str6.isidentifier())

# print(str6.ljust(20), 'hello')

# SHOK
# Делает большие символы маленькиими и наоборот
# print(str6.swapcase())
# возвращает каждую строку как элемент списка
# print(str6.splitlines())
# Возвращает три элемента в tuple = Левую часть / аргумент / правую часть
# print(str6.rpartition('adfasa'))
# print(str6.translate())

# Если проворачивать вот такой трюк то берет самое правое значение
str7 = "I could eat bananas all day, bananas are my favorite fruit"
# print(str7.rpartition('bananas'))
