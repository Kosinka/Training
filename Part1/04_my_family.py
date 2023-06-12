#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Me', 'Dad', 'Mom']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 180],
    [my_family[1], 175],
    [my_family[2], 160],
]
dad = my_family_height[1]
dad_heigth = dad[1]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца: - ' + str(dad_heigth))

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
heigth = 0
for family_member in my_family_height:
    heigth += family_member[1]

print(heigth)
