'''
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
'''


def neutralise(s1, s2):
	return ''.join([i1 if i1 == i2 else '0' for i1, i2 in zip(s1, s2)])


print(neutralise("+-+", "+--"))

'''
neutralise("--++--", "++--++") ➞ "000000"

neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"

neutralise("-++-", "-+-+") ➞ "-+00"
'''
