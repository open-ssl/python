'''
Your function will be passed two functions, f and g, that don't take any parameters.
Your function has to call them, and return a string which indicates which function returned the larger number.

If f returns the larger number, return the string f.
If g returns the larger number, return the string g.
If the functions return the same number, return the string neither.
'''

def which_is_larger(f, g):
    return 'g' if f() < g() else 'f' if f() > g() else 'neither'


# which_is_larger(lambda: 5, lambda: 10) ➞ "g"
# which_is_larger(lambda: 25,  lambda: 25) ➞ "neither"
# which_is_larger(lambda: 505050, lambda: 5050) ➞ "f"
