def func():
    for i in range(1, 20):
        a = [i, 'Fizz'][i%3 == 0]
        if isinstance(a, int):
            print([i, 'Buzz'][i%5 == 0])
            continue
        print([a, a + 'Buzz'][i%5 == 0])

func()
