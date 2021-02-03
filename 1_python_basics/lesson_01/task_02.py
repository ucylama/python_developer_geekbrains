user_input = int(input('Введите количество секунд: '))

hours = user_input // 3600 # добавить % 24 для получения "текущего" времени
minutes = user_input // 60 % 60
seconds = user_input % 60

print(f'{hours}:'
      f'{minutes // 10}{minutes % 10}'
      f':{seconds // 10}{seconds % 10}')
