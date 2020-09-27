
import datetime
def get_days(d1, d2):
    return (d2 - d1).days
# print(dir(datetime.date))

# def get_days(date1, date2):

#
# print(get_days(
#   datetime.date(2019, 6, 14),  # June 14, 2019
#   datetime.date(2019, 6, 20)  # June 20, 2019
# ))
#
#
# get_days(
#   datetime.date(2019, 6, 14),  # June 14, 2019
#   datetime.date(2019, 6, 20)  # June 20, 2019
# ) ➞ 6
#
#
# get_days(
#   datetime.date(2018, 12, 29),  # December 29, 2018
#   datetime.date(2019, 1, 1)  # January 1, 2019
# ) ➞ 3
# # Dates may not all be in the same month/year.
#
#
# get_days(
#   datetime.date(2020, 5, 24),
#   datetime.date(2019, 5, 24))
# ) ➞ -366
# Backwards dates should return a negative change.
