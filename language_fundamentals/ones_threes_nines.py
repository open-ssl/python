'''
Given an int, figure out how many ones, threes and nines you could fit into the number.
You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this.
'''


class ones_threes_nines():
    def __init__(self, num):
        self.num=num
        self.nines=num//9
        self.ones=num
        self.threes=num//3


# n = ones_threes_nines(5)
# print(n.nines)
# print(n.ones)
# print(n.threes)
