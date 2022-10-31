import random

def Enter_number(text, type = 1): # функция ввода числа с проверкой 
    print(text)
    while True:
        if type == 1:
            try:
                value = int(input())
                break
            except:
                print("Ошибка! Введите целое число:")
        elif type == 2 or type == 3:
            try:
                if type == 2:
                    value = float(input())
                    break
                elif type == 3:
                    from decimal import Decimal
                    value = Decimal(input())
                    break
            except:
                print("Ошибка! Введите число:")
    return value

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
number = abs(Enter_number("Введите вещественное число:", 3))

while number % 1 != 0:
    number *= 10

number_sum = 0
while number >= 1:
    number_sum += number % 10
    number = number // 10

print(f'Сумма цифр этого числа равна {int(number_sum)}')
print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number_count = abs(Enter_number("Введите целое положительное число:"))

new_element = 1
numbers_list = [new_element]

for i in range(2, number_count + 1):
    new_element *= i
    numbers_list.append(new_element)

print(f'Произведения чисел от 1 до {number_count}:\n{numbers_list}')
print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

dict_size = abs(Enter_number("Введите целое положительное число:"))
numbers_dict = {n : round(pow((1 + 1 / n), n), 2) for n in range(1, dict_size + 1)}

values_sum = 0
for j in numbers_dict.values():
    values_sum += j
    
print(f'Для n = {dict_size} {numbers_dict}')
print(f'Сумма значений = {round(values_sum, 3)}')

print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt - в одной строке одно число.

N = abs(Enter_number("Введите целое число N:"))

interval_list = []
for k in range(1, N + 1):
    interval_list.append(random.randint(-N, N))

print(f'{N} случайных элементов со значениями от {-N} до {N}: {interval_list}')

multiplication_of_position = 1
print('Для значений по указанным в файле индексам:')
data = open('file.txt', 'r')
for line in data:
    i = int(line.replace('\n', ''))
    if i < N:
        print(f'{[i]} = {interval_list[i]}')
        multiplication_of_position *= interval_list[i]
    else:
        print(f'{[i]} - нет элемента')
data.close

print(f'произведение равно: {multiplication_of_position}')

print(input('Для перехода к следующей задаче нажмите "Enter"'))

# 5. Реализуйте алгоритм перемешивания списка.

list_length = abs(Enter_number("Введите количество элементов списка:"))

list_for_random =[]
for i in range(list_length):
    list_for_random.append(i + 1)

print(f'Список c {list_length} элементами: {list_for_random}')

temp = list_for_random[0]
for i in range(list_length):
    a = random.randint(0, list_length - 1)
    b = random.randint(0, list_length - 1)
    temp = list_for_random[b]
    list_for_random[b] = list_for_random[a]
    list_for_random[a] = temp

print(f'Перемешанный список: {list_for_random}')