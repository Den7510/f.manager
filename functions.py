mixed = ['мак', 'горох', 'мак', 'мак', 'просо', 'рис', 'гречка', 'просо', 'просо', 'мак']
zolushka = list(filter(lambda x: x == 'мак', mixed))

l1 = [1, 2, 3]
l2 = [4, 5, 6]
new_list = list(map(lambda x, y: x + y, l1, l2))

m = [7, 4, 9, 5]
r = [7, 8, 9, 4]
sort = list(sorted(map(lambda x, y: x+y, m, r)))

import math
'''
вычисляем площадь круга
'''
def sq(r):
    x = math.pi
    y = math.pow(r, 2)
    return x*y

'''извлекаем корень'''

z = math.sqrt(81)

'''находим гипотинузу'''
t = math.hypot(7, 7)

