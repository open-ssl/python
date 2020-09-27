def lambda_depth(num):
    return 'edabit' if num == 0 else lambda: lambda_depth(num-1)
 # = lambda x: 'edabit' if x == 0 else lambda_depth(num-1)
 # = lambda x : 'edabit' if x == 0 else lambda_depth(x-1)

print(lambda_depth(0))
# "edabit"

print(lambda_depth(1)())
 # ➞ "edabit"

print(lambda_depth(2)()())
 # ➞ "edabit"

# type(lambda_depth(2)()) ➞ <class: "function">
