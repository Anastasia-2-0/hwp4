# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

stepen = (input("Введите натуральную степень: "))
stepen = int(stepen)
result = ''
for i in range(stepen, 0, -1):
    a = '*x^' + str(i)
    result += (str(randint(0, 100)) + a + ' + ')
polinomial = result + str(randint(0, 100)) + '= 0'
data = open('task_019.txt', 'w')
data.writelines(polinomial)
data.close()
with open('task_019.txt', 'r') as data:
    print(
        f'Многочлен степени "{stepen}" = {data.readlines()}')