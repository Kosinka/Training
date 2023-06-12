#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

print(round(math.pi * radius ** 2, 2))

# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

zero_coordinate_x, zero_coordinate_y = 0, 0
point_x, point_y = point[0], point[1]
point_distance = ((point_x - zero_coordinate_x) ** 2 + (point_y - zero_coordinate_y) ** 2) ** 0.5
print(point_distance <= radius)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

point_2_x, point_2_y = point_2[0], point_2[1]
point2_distance = ((point_2_x - zero_coordinate_x) ** 2 + (point_2_y - zero_coordinate_y) ** 2) ** 0.5
print(point2_distance <= radius)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


