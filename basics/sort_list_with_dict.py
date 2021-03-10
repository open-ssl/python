# def func(drinks):
    # return sorted(drinks, key=lambda x: x.get('price'))

def func(drinks):
    _lst = [item.get('price') for item in drinks]
    return sorted(_lst)
    # return [drink for it in _lst for drink in drinks if drink.get('price') == it]
    # for item in _lst:
        # for drink_item in drinks:
            # if drink_item.get('price') == item:
                # result_lst.append(drink_item)

    # return result_lst
#
drinks = [
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10},
  {"name": "lemonade33", "price": 250},
  {"name": "lemonade23", "price": 150},
]
print(func(drinks))
