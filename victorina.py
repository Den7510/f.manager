def viktorina():
    str = 'да'
    while str == 'да':
        names = {1: 'H Kolumb', 2: 'A Enchtein',
                 3: 'A Puchkin', 4: 'L Paster',
                 5: 'G Galilei', 6: 'W Shekspir',
                 7: 'L De Vinchi', 8: 'A Mozart',
                 9: 'I Newton', 10: 'G Leibniz'
                 }
        mounts = {'01': 'января', '02': 'февраля', '03': 'марта',
                  '04': 'апреля', '05': 'мая', '06': 'июня',
                  '07': 'июля', '08': 'августа', '09': 'сентебря',
                  '10': 'октября', '11': 'ноября', '12': 'декабря'
                  }
        days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
                '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
                '11': 'одинадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
                '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
                '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
                '23': 'двадцать третье', '24': 'двадцать четвёртое', '25': 'двадцать пятое', '26': 'двадцать шестое',
                '27': 'двадцать седьмое', '28': 'двадцатьт восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое'
                }
        yars = [1451, 1879, 1799, 1822, 1564, 1564, 1452, 1756, 1643, 1646]
        import random
        numbers = [names[1], names[2], names[3], names[4], names[5], names[6], names[7], names[8], names[9], names[10]]
        result = random.sample(numbers, 5)
        print(result)
        correct = []
        incorrect = []
        day = 0
        mount = 0
        year = 0
        for name in result:
            if result[0] == names[1]:
                print(names[1])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '31.10.1451'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['31']
                    mount = mounts['10']
                    yar = yars[0]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[2]:
                print(names[2])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '14.03.1879'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['14']
                    mount = mounts['03']
                    yar = yars[1]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[3]:
                print(names[3])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '06.06.1799'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['06']
                    mount = mounts['06']
                    yar = yars[2]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[4]:
                print(names[4])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.12.1822'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['12']
                    yar = yars[3]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[5]:
                print(names[5])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.02.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['15']
                    mount = mounts['02']
                    yar = yars[4]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[6]:
                print(names[6])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '26.04.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[5]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[7]:
                print(names[7])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.04.1452'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[6]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[8]:
                print(names[8])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.01.1756'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['01']
                    yar = yars[7]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[9]:
                print(names[9])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '04.01.1643'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['04']
                    mount = mounts['01']
                    yar = yars[8]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[0] == names[10]:
                print(names[10])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '01.07.1646'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['01']
                    mount = mounts['07']
                    yar = yars[9]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
        for name in result:
            if result[1] == names[1]:
                print(names[1])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '31.10.1451'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['31']
                    mount = mounts['10']
                    yar = yars[0]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[2]:
                print(names[2])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '14.03.1879'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['14']
                    mount = mounts['03']
                    yar = yars[1]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[3]:
                print(names[3])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '06.06.1799'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['06']
                    mount = mounts['06']
                    yar = yars[2]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[4]:
                print(names[4])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.12.1822'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['12']
                    yar = yars[3]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[5]:
                print(names[5])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.02.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['15']
                    mount = mounts['02']
                    yar = yars[4]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[6]:
                print(names[6])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '26.04.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[5]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[7]:
                print(names[7])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.04.1452'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[6]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[8]:
                print(names[8])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.01.1756'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['01']
                    yar = yars[7]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[9]:
                print(names[9])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '04.01.1643'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['04']
                    mount = mounts['01']
                    yar = yars[8]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[1] == names[10]:
                print(names[10])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '01.07.1646'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['01']
                    mount = mounts['07']
                    yar = yars[8]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
        for name in result:
            if result[2] == names[1]:
                print(names[1])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '31.10.1451'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['31']
                    mount = mounts['10']
                    yar = yars[0]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[2]:
                print(names[2])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '14.03.1879'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['14']
                    mount = mounts['03']
                    yar = yars[1]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[3]:
                print(names[3])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '06.06.1799'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['06']
                    mount = mounts['06']
                    yar = yars[2]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[4]:
                print(names[4])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.12.1822'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['12']
                    yar = yars[3]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[5]:
                print(names[5])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.02.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['15']
                    mount = mounts['02']
                    yar = yars[4]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[6]:
                print(names[6])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '26.04.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[5]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[7]:
                print(names[7])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.04.1452'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[6]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[8]:
                print(names[8])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.01.1756'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['01']
                    yar = yars[7]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[9]:
                print(names[9])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '04.01.1643'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['04']
                    mount = mounts['01']
                    yar = yars[8]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[2] == names[10]:
                print(names[10])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '01.07.1646'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['01']
                    mount = mounts['07']
                    yar = yars[9]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
        for name in result:
            if result[3] == names[1]:
                print(names[1])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '31.10.1451'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['31']
                    mount = mounts['10']
                    yar = yars[0]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[2]:
                print(names[2])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '14.03.1879'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['14']
                    mount = mounts['03']
                    yar = yars[1]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[3]:
                print(names[3])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '06.06.1799'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['06']
                    mount = mounts['06']
                    yar = yars[2]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[4]:
                print(names[4])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.12.1822'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['12']
                    yar = yars[3]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[5]:
                print(names[5])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.02.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['15']
                    mount = mounts['02']
                    yar = yars[4]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[6]:
                print(names[6])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '26.04.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[5]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[7]:
                print(names[7])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.04.1452'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[6]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[8]:
                print(names[8])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.01.1756'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['01']
                    yar = yars[7]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[9]:
                print(names[9])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '04.01.1643'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['04']
                    mount = mounts['01']
                    yar = yars[8]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[3] == names[10]:
                print(names[10])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '01.07.1646'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['01']
                    mount = mounts['07']
                    yar = yars[9]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
        for name in result:
            if result[4] == names[1]:
                print(names[1])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '31.10.1451'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['31']
                    mount = mounts['10']
                    yar = yars[0]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[2]:
                print(names[2])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '14.03.1879'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['14']
                    mount = mounts['03']
                    yar = yars[1]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[3]:
                print(names[3])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '06.06.1799'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['06']
                    mount = mounts['06']
                    yar = yars[2]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[4]:
                print(names[4])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.12.1822'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['12']
                    yar = yars[3]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[5]:
                print(names[5])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.02.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['15']
                    mount = mounts['02']
                    yar = yars[4]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[6]:
                print(names[6])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '26.04.1564'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[5]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[7]:
                print(names[7])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '15.04.1452'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['26']
                    mount = mounts['04']
                    yar = yars[6]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[8]:
                print(names[8])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '27.01.1756'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['27']
                    mount = mounts['01']
                    yar = yars[7]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[9]:
                print(names[9])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '04.01.1643'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['04']
                    mount = mounts['01']
                    yar = yars[8]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
            elif result[4] == names[10]:
                print(names[10])
                print('Введите дату рождения в формате dd.mm.yyyy:')
                data = '01.07.1646'
                day, mount, year = data.split('.')
                option1 = input()
                if option1 != data:
                    incorrect.append(option1)
                    day = days['01']
                    mount = mounts['07']
                    yar = yars[9]
                    print(day, mount, yar, 'года')
                elif correct.append(option1):
                    print(day, mount, yar, 'года')
                break
        # print(incorrect)
        # print(correct)
        print('Неправильных ответов: ')
        print(len(incorrect))
        print('Правильных ответов: ')
        print(len(correct))
        str1 = 'нет'
        print('Хотите продолжить отгадывать векторину? ')
        if input() == str1:
            print('end')
            break
        else:
            continue


