try:
    str1 = 'нет'
    print('Хотите продолжить отгадывать векторину? ')
    if input() == str1:
        print('end')
except ValueError:
    print('введите ответ верно')
