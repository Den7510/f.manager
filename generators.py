import random
names = [ 'H Kolumb',  'A Enchtein',
                  'A Puchkin', 'L Paster',
                  'G Galilei',  'W Shekspir',
                  'L De Vinchi',  'A Mozart',
                  'I Newton',  'G Leibniz'
         ]
for name in names:
    result = [random.sample(names, 5) if name == 'L De Vinchi' in names else 'H Kolumb']
    print(result)

yars = [1451, 1879, 1799, 1822, 1564, 1564, 1452, 1756, 1643, 1646]
summ = []
new_yars = random.sample(yars, 5)
for data in new_yars:
    if data > 1440 and data < 1600:
        summ.append(data)
print(summ)

summ = [data for data in new_yars if data > 1440 and data < 1600]
print(summ)

summ = filter(lambda new_yars: 1440 < new_yars < 1600, new_yars)
print(list(summ))

name_a =[name for name in names if name.startswith('G')]
print(name_a)

name_a =[name for name in names if name[3] == 'a']
print(name_a)

result = {name:int(len(name)) for name in names}
print(result)

