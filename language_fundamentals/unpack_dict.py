'''For each challenge of this series you do not need to submit a function.
Instead, you need to submit a template string that can formatted in order to get a certain outcome.

Write three dictionaries and a template string according to the following example.
Notice the article "a" in the third example:
'''

dic1 = {"action": "like",
        "name": "Mary",
        "name2": 'May'}
dic2 = {"action": "love",
        "name": "Eda",
        "name2": 'Bit'}
dic3 = {"action": "have",
        "name": "a Pidgey",
        "name2": 'a Rattata'}
template = "I {action} {name}, I don't {action} {name2}."

# template.format(**dic1) ➞ "I like Mary, I don't like May."
# template.format(**dic2) ➞ "I love Eda, I don't love Bit."
# template.format(**dic3) ➞ "I have a Pidgey, I don't have a Rattata."


print(template.format(**dic1))
print(template.format(**dic2))
print(template.format(**dic3))

# product = {"name": "pokeball", "price": 20}
# "One {name} is ${price:.2f}".format(**product) ➞ "One pokeball is $20.00"
