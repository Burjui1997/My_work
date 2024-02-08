# string = "hello, world!"
#
# print(string.lower())
# print(string.strip())
# print(string.upper())
# print(string.replace(',', '!').upper())
# print(string.split(','))
# print(string.replace('hello', 'piska').upper())
# print(string.strip('hel'))
# print(string.find('hello'))
# print(string.index(' world'))
import string

# pip = """
# Не о лице думай, думай об имени
# Без имени и овца баран
# Лучше глаза лишиться, чем доброго имени
# Имя хорошего человека не забывается
# Золото не останется в земле, доброе имя не померкнет в народе
# Доброе имя береги — запятнаешь, от людей не скроешь
# Лучше разбить себе голову, чем разбить свое доброе имя
# Доброе имя лучше богатства
# Доброе имя лучше сокровищ
# От хорошего человека остается имя, от плохого — дурной пример
# Имя какое бы ни было — был бы хорош, кто его носит
# После смерти у человека остается имя, а у медведя — шкура
# От мертвого коня подкова останется, от храбреца — славное имя
# Чем опорочить свое имя, лучше переломить себе кость
# """
# # string2 = "айфон"
# # print(string.replace('голову', string2))
# # print(string.index(string2))
# # proverb = (input("Введите пословицу:"))
# word = (input("Введите слово которое хотите заменить:"))
# word2 = (input("Введите новое слово:"))
# new_pro = (pip.replace(word, word2).upper("word2"))
# print(new_pro)

user_name = 'Igor1997'
print(user_name.isdigit())
print(user_name.isalpha())
print(user_name.isalnum())
if user_name.isalpha() != True:
    print('Только буквы')


# shop_list = ['молоко', 'квартира', 'банан', 'банан', ]
# print(len(shop_list))
# print(shop_list[3])
# print(shop_list[0:2]) # срез списка
# shop_list[0] = 'сок'
# print(shop_list)

# phone_number = input("Введите номер телефона: ")
# phone_number = phone_number.strip()
# phone_number = phone_number.replace
# if len(phone_number)!= 11:
#     print("Неверный номер телефона")
# if phone_number.startswith("+7") and phone_number.startswith("8"):
#     print("правильный номер телефона")
#
# if phone_number.isdigit():
#     print("правильный номер телефона")
# else:
#     print("неправильный номер телефона")


print('+7(777) 731 83 58'.replace(' ',''))