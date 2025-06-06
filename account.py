"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def start():
    # Инициализация переменных
    balance = 0  # Баланс счета
    purchase_history = []  # История покупок

    while True:
        # Вывод меню
        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        # Выбор пункта меню
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            # Пополнение счета
            try:
                amount = float(input('Введите сумму для пополнения счета: '))
                if amount > 0:
                    balance += amount
                    print(f'Счет успешно пополнен на {amount}. Текущий баланс: {balance}')
                else:
                    print('Сумма должна быть положительной.')
            except ValueError:
                print('Ошибка ввода. Введите корректное число.')

        elif choice == '2':
            # Покупка
            try:
                purchase_amount = float(input('Введите сумму покупки: '))
                if purchase_amount > balance:
                    print('Недостаточно средств на счете.')
                elif purchase_amount <= 0:
                    print('Сумма покупки должна быть положительной.')
                else:
                    purchase_name = input('Введите название покупки: ')
                    balance -= purchase_amount
                    purchase_history.append((purchase_name, purchase_amount))
                    print(f'Покупка "{purchase_name}" на сумму {purchase_amount} успешно совершена.')
                    print(f'Текущий баланс: {balance}')
            except ValueError:
                print('Ошибка ввода. Введите корректное число.')

        elif choice == '3':
            # История покупок
            if not purchase_history:
                print('История покупок пуста.')
            else:
                print('История покупок:')
                for item in purchase_history:
                    print(f'{item[0]} - {item[1]}')

        elif choice == '4':
            # Выход из программы
            print('Выход из программы.')
            break

        else:
            # Обработка неверного выбора
            print('Неверный пункт меню.')

if __name__ == "__main__":
    start()
