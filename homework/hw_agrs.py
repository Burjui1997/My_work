def chek_palindrom(*args):
    results = []
    for arg in args:
        if arg == arg[::-1]:
            results.append({arg: True})
        else:
            results.append({arg: False})
    return results

user_input = input('Введите слова через пробел: ').split()
check_func = chek_palindrom(*user_input)
print(check_func)




