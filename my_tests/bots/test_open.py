with open('/Users/stanislavlukanov/Desktop/LEARN/python/python/my_tests/bots/en_words/level1.txt', 'r') as f:
    file = f.readlines()
    for row in file:
        key, word = row.split(' ')
        print(key)
        print(word)
