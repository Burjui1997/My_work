temp = int(input('Температура в градусах цельсия: '))
kelvin = temp + 274
fahrenheit = (temp * 9/5) + 32
reaumur = temp * 4/5

print(f'Температура в градусах цельсия: {temp} градусов \n'
      f'{kelvin} градусов \n'
      f'{fahrenheit} градусов \n'
      f'{reaumur} градусов')