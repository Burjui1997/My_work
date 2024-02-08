# string = "Hello World!"
#
# for letter in string:
#     if letter != ' ':
#         print(letter, end='')

# product_list = ['молоко,мясо,рыба,фасоль,бананы']
# bad_list = ['молоко,мясо,рыба']
#
# new_list = ['молоко,мясо,рыба']
# for product in product_list:
#     new_list.append(product)
# new_list = []
# for product in new_list:
#     if product not in bad_list:
#         new_list.append(product)
# new_list = [product for product in product_list if product not in bad_list]
# print(new_list)

users_lst = ['John88', 'Legolas123', 'YagamiLight','Catwoman', 'Dragonborn', 'Daenerys','Nagibator228', 'BigDaddy','Killer007',
'Сергей']
nums_users = []
for user in users_lst:
     if not user.isalpha():
         nums_users.append(user)
         users_lst.remove(user)

print(nums_users)
print(users_lst)