# summ = 5+5
# print(f'сумма: {summ}')


# a = 5
# b = 3
# print(a > b)

# print(a!=b)

# minuts = int(input('введите минуты: '))
# hours = minuts // 60
# print (f'часы :{hours}')

# name = 'Иван'
# name2 = 'Иван'
# print(name == name2)
# print(name is name2)
#
# print(f'Проверяем выражение "2>3 и 3<5": {5>2 and 5>2}')

# name = 'Иван'
 # age =  30
# print(f'"name=="Иван" and age==30": {name == "Иван" and age == 30}')

# name = input('Введите имя: ')
# print(f'Вход разрешен: {not(name == "Иван" or name == "иван" or name == "Ivan")}')

# name = int(input('Введите возраст: \n'
#                  'Введите имеющиеся долги:\n'
#                  'Введите доход :\n'
#                  'Введите желаемую сумму кредита:\n'
#                  'Введите срок кредита:'))
age= int(input('Введите возраст: '))
money = int(input('Введите доход: '))
credit = int(input('Введите сумму кредита: '))
srokcredit = int(input('Введите срок кредита: '))
dolgi = int(input('Введите имеющиеся долги: '))
creditpayer = (credit/srokcredit)
print(f'Ваше решение по кредиту:{(age>18 or age<=75) and creditpayer >= money*0.5 and dolgi ==0 }')
