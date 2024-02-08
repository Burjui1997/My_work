data_lst = ['1', '2', 15, '3', 5, '4', '5', 2, 'Hello World']
empty_list = []

for i in data_lst:
    try:
        empty_list.append(int(i))
    except ValueError:
        print(f"Invalid value {i}")
print(empty_list)


