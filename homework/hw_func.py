# Пересечение списков
def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements_set = set1.intersection(set2)
    common_elements = list(common_elements_set)
    return common_elements


list1 = [1, 2, 3, 4]
list2 = [2, 5, 1, 6]
result = common_elements(list1, list2)
print(result)
# Количество гласных и согласных:
def count_vowels_and_consonants(input_str):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч',
                  'ш', 'щ']
    input_str = input_str.lower()
    vowel_count = 0
    consonant_count = 0
    for i in input_str:
        if i in vowels:
            vowel_count += 1
        elif i in consonants:
            consonant_count += 1
    return vowel_count, consonant_count

input_str =  str(input('Введите что хотите:'))
vowels_count, consonants_count = count_vowels_and_consonants(input_str)
print(f'Гласных букв:{vowels_count},согласных букв:{consonants_count}')

# Самая длинная строка:

def find_string(str_list):
    if not str_list:
        return None
    longest_string = str_list[0]
    for string in str_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

str_list = ['Игорь','Учит','Пайтон','Вроде','Получается']
result = find_string(str_list)
print(result)
