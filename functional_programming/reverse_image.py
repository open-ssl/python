'''
Suppose an image can be represented as a 2D list of 0s and 1s.
Create a function to reverse an image. Replace the 0s with 1s and vice versa.
'''

def reverse_image(lst):
    def func(item):
        return [0 if i == 1 else 1 for i in item]

    return list(map(func, [i for i in lst]))

print(reverse_image([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]))
