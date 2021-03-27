# читаем из файла
f = open("stas.txt",'r')
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()
# итеративно читаем из файла
print()
for line in open("stas.txt", 'r'):
    print(line, end='')

# пишем в файл
# f = open('stas.txt', mode='w')
# text_list = ['this', 'is', 'new', 'text']
# for item in text_list:
#     print(item, file=f)
# f.close()

# новый контент
print('new data!!')
# f = open('stas.txt', mode='r')
for item in open('stas.txt', mode='r'):
    print(item, end='')
