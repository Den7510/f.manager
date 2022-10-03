def account():
    bill_sum = 0
    history = []
    with open('bill_sum.txt', 'r') as f:
       order_old = int(f.read())
    with open('purchases.txt', 'r') as f:
        for name in f:
            history.append(name.replace('\n',''))

    def buy(order_old):
        cost = int(input('Введите сумму покупки'))
        if cost > order_old:
            print('Недостаточно средств')
        else:
            order_old -= cost
            name = input('Введит название покупки')
            with open('purchases.txt', 'a') as f:
                purchases = f.write(f'{name}\n')
            history.append((name, cost))
        return order_old

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {order_old}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            cost = int(input('Введите сумму'))
            order_old += cost
            with open('bill_sum.txt', 'w') as f:
                f.write(f'{order_old}')
        elif choice == '2':
            order_old = buy(order_old)
        elif choice == '3':
            print(history)
        elif choice == '4':
            with open('bill_sum.txt', 'w') as f:
                f.write(f'{order_old}')
            break
        else:
            print('Неверный пункт меню')

