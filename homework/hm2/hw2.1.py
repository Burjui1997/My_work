seconds = int(input('Введите количество секунд: '))
hours = seconds // 3600
minutes = (seconds % 3600)//60
seconds = (seconds % 60)%60


print(f'В указанном формате секунд: {hours} часов, {minutes} минут, {seconds} секунд')