# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def number_simple(n: int):
    i = 2
    while n % i != 0 or i == n - 1:
        i += 1
    if i == n:
        return n

def fill_number(n: int) -> list:
    my_list = [1]
    for i in range(2, n+1):
        if n % i == 0:
            if number_simple(i) != None:
                my_list.append(number_simple(i))
            else:
                continue
    return my_list


n = int(input('Введите натуральное число: '))
my_list = fill_number(n)
print(my_list)