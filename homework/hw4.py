num = input('Введите номер телефона: ')
num_check = num.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
num_check = len(num_check) == 11
if num_check:
    print('Номер введен верно ! Ура! ')
else:
    print('Упс.. Повторите еще раз!')


password = input('Введите валидный пароль: ')
if len(password) > 7:
    if not password.find('_') == -1 or not password.find('*') == -1:
        print(f'Вы ввели валидный пароль:  {password.replace(" ", "")}')
    else:
        print('Вы ввели недостаточно валидный пароль')
else:
    print('Попробуйте еще раз')
