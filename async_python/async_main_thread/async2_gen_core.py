from time import time
# generators = function  with next()

def gen1(name):
    for it in name:
        yield it

# g = gen('Stas')


# def gen_filename():
#     while True:
#         pattern = 'file {}.jpeg'
#         t = int(time() * 1000)
#         yield pattern.format(str(t))
#         # вызовется следующим после next
#         yield 'STAS'
#         yield 'STASEN'
#         yield 'STASEEEEK'



def gen2(num):
    for item_num in range(num):
        yield item_num


g1 = gen1('stas')
g2 = gen2(4)


tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
