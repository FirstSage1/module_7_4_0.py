# module_7_4.py Форматирование строк
# ====================================

# Исходные данные
team1_num = 5  # количество участников первой команды
team2_num = 6  # количество участников второй команды
score1 = 40  # количество задач решенных первой командой
score2 = 42  # количество задач решенных второй командой
team1_time = 1552.512  # время за которое команда 1 решила задачи
team2_time = 2153.31451  # время за которое команда 2 решила задачи
tasks_total = score1 + score2  # количество задач решенных обеими командами
time_avg = (team1_time + team2_time) / tasks_total  # среднее время решения 1-й задачи
# tasks_total = 82
# time_avg = 45.2

# Условия победы команды
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Использование %:
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование format():
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))

# Использование f-строк:
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')