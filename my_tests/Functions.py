def func(*args):
    print(args[0])
    print(args[1])
    print(args[2])

def func1(**kwargs):
    print(kwargs['name'])
    print(kwargs['name1'])
    print(kwargs['name1'])
    print(kwargs['name2'])




name = 1
name1 = 5
name2 = 10


func1(name=name, name1=name1, name2=name2)
func('First arg', 'Hello', 'Stas')


# A lambda function can take any number of arguments,
# but can only have one EXPRESSION.

# The power of lambda is better shown when you use
# them as an anonymous function inside another function.

lambda a: a + 10

lambda a, b, c: a + b + c


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
