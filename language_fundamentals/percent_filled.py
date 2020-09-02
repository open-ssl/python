def percent_filled(box):
	box = ''.join(box)
	items_sum = box.count('o') + box.count(' ')
	return '{}%'.format(str(int(round((box.count('o') / items_sum), 2) * 100)))


print(percent_filled([
   "######",
  "#ooo #",
  "#oo  #",
  "#    #",
  "#    #",
  "######"
]))
