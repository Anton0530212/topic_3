# Программа, которая запрашивает у пользователя
# его имя и возраст (целое число),
# а затем выводит приветственное сообщение
name: str = input('Введите ваше имя: ')
age: int = int(input('Введите ваш возраст: '))

greeting: str = 'Привет, ' + name + '! Тебе уже ' + str(age) + ' лет!'

print(greeting)
