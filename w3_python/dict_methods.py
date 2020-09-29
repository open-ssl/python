# Dicts

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thedict1 = dict({
    1: 2,
    'stas': 'stas'
})
print(thedict1)

# Get values from dict
# two ways

print(thisdict['brand'])
print(thisdict.get('brand'))


# by default the dict loops by key
for i in thisdict:
    print(i)

# all elements
for key, value in thisdict.items():
    print([key, value])




# check key in dict
'key' in thisdict


# for removing item
# del thisdict['key']
# thisdict.pop('key')

# BUT
# thisdict.popitem() removes last inserted value

# removes all
# thisdict.clear()

dct2 = thisdict.copy()
dct3 = dict(thisdict)

print(dct2)


# Wow
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
