word = input("Введите слово: ")
revers_word = word[::-1]

if word.lower() == revers_word.lower():
    print(f"Обнаружен палиндром: {word}")
else :
    print(f"Слово {word} палиндромом не является")