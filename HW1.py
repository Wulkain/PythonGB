import math
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# -  -> нет 

print('Введите число, обозначающее день недели')
numDay = int(input())

if (numDay == 6 or numDay == 7): print ('Yes')
    
elif (numDay < 6): print ('No')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер  ,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 
# - x=-34; y=-30 -> 3

print('Введите координату точки по оси X:')
x = float(input())

print('Введите координату точки по оси Y:')
y = float(input())

if x != 0 and y != 0:
    if x > 0 and y > 0: print('Эта точка находится в 1  квадранте ')
    elif x < 0 and y > 0: print('Эта точка находится во 2  квадранте ')
    elif x < 0 and y < 0: print('Эта точка находится в 3  квадранте ')
    else: print('Эта точка находится в 4  квадранте ')
else:
    if x == 0 and y != 0: print('Эта точка находится на квадранте оси Y')
    elif x != 0 and y == 0: print('Эта точка находится на квадранте оси X')
    else: print("Точка находится в начале координат")

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер квадранта:')
cuartNum = int(input())

if cuartNum == 1: print(f'В {cuartNum} квадранте возможный диапазон координат точек:\n X>0, Y>0')
elif cuartNum == 2: print(f'В {cuartNum} квадранте возможный диапазон координат точек:\n X<0, Y>0')
elif cuartNum == 3: print(f'В {cuartNum} квадранте возможный диапазон координат точек:\n X<0, Y<0')
elif cuartNum == 4: print(f'В {cuartNum} квадранте возможный диапазон координат точек:\n X>0, Y<0')
else: print('Введен некорректный номер квадранта.')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print ('Введите значение X первой координаты:')
x1 = int(input())

print ('Введите значение Y первой координаты:')
y1 = int(input())

print ('Введите значение X второй координаты:')
x2 = int(input())

print ('Введите значение Y второй координаты:')
y2 = int(input())

distance = round(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)), 2)
print(f'Расстояние между  точками с координатами ({x1};{y1}) и ({x2};{y2}) равно {distance}')



# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x3 in True, False:
    for y3 in True, False:
        for z3 in True, False:
            if ((x3 or y3 or z3) == (not(x3) and not(y3) and not(z3))):
                print ("True")
            else:
                print ("False")