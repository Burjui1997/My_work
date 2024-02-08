# +77053183958;+77773183958;87773183958;+(777)73183958;+7(777)-731-83-58;+7(777) 731 83 58

phone_str = input("Введите номера телефонов без пробелов, разделяя их символом ';' ")


phone_list = phone_str.split(";")

for i in phone_list:
    #todo очистить i от всего
    print(i.replace(" ", "").replace("-","").replace("(","").replace(")","").replace("+",""))
    if len(i) != 11 and i[0] != 8 and i.startswith('+7') is False:
        raise ValueError(f'номер {i} больше 11 знаков')



