# '''
# When importing objects from a module in Python, the syntax usually is as follows:
#
# from module_name import object
# Given a string of an incorrect import statement, return the fixed string. All import statements will be the wrong way round.
# '''
# def fix_import(txt):
#     index = txt.find('from')
#     return txt[index:] + ' ' + txt[:index]
#     # return (' '.join(txt[2:]) + ' ' + ' '.join(txt[:2]))
# # fix_import("import object from module_name") ➞ "from module_name import object"
#
# # fix_import("import randint from random") ➞ "from random import randint"
#
# print(fix_import("import pi from math"))
#  # ➞ "from math import pi"



print('import pi from math'.split())
