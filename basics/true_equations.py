'''
In this challenge you will be given a list containing equations, with each equation written as a string. Here's an example:

["1+1=2", "2+2=3", "5*5=10", "3/3=1"]
If you do the math, you'll see that the equations "1+1=2" and "3/3=1" are actually true while "2+2=3" and "5*5=10" are false nonsense.

Write a function which, given a list of equations as above, returns only the true equations. For instance, for the example above the output should be:

["1+1=2", "3/3=1"]
'''


def true_equations(lst):
    return [i for i in lst if eval(i.replace('=', '=='))]

print(true_equations(["2*2=4"]))
#  ["2*2=4"]

print(true_equations(["1+1=3", "3-1=1"]))
 # ➞ []

# true_equations(["1+1=2", "2+2=3", "5*5=10", "3/3=1"]) ➞ ["1+1=2", "3/3=1"]
