# Программа, которая запрашивает у пользователя
# почасовую ставку, затем выводит его количество
# отработанных часов и заработную плату

hourly_rate: float = float(input('Введите почасовую ставку: '))

working_hours: int = 22 * 8
salary: float = hourly_rate * working_hours

print('Вы проработали', working_hours, 'часов')
print('Ваша зарплата в месяц:', salary, 'рублей')
