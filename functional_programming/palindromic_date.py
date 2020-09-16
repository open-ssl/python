'''
The 2nd of February 2020 is a palindromic date in both dd/mm/yyyy and mm/dd/yyyy
format (02/02/2020). Given a date in dd/mm/yyyy format, return True if the date
is palindromic in both date formats, otherwise return False.
'''
def palindromic_date(date):
    d, m, y = date.split('/')
    d, m = d[::-1], m[::-1]
    return d + m == y and m + d == y

# Although 11/02/2011 is palindromic in dd/mm/yyyy format,
# it isn't in mm/dd/yyyy format (02/11/2011)

print(palindromic_date("02/02/2020"))
  # True

# palindromic_date("11/12/2019")  False

print(palindromic_date("11/02/2011"))
# False
