'''
Given a dictionary of some items with star ratings and a specified star rating,
return a new dictionary of items which match the specified star rating.
Return "No results found" if no item matches the star rating given.
'''


def filter_by_rating(dct, rating):
    return_dct = dict([i for i in dct.items() if i[1] == rating])
    return return_dct if return_dct else 'No results found'


print(filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****"))



'''
filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****") ➞ {
  "Luxury Chocolates" : "*****",
  "Aunty May Chocolates" : "*****"
}

filter_by_rating({
  "Continental Hotel" : "****",
  "Big Street Hotel" : "**",
  "Corner Hotel" : "**",
  "Trashviews Hotel" : "*",
  "Hazbins" : "*****"
}, "*") ➞ {
  "Trashviews Hotel" : "*"
}

filter_by_rating({
  "Solo Restaurant" : "***",
  "Finest Dinings" : "*****",
  "Burger Stand" : "***"
}, "****") ➞ "No results found"
'''
