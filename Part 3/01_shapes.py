# -*- coding: utf-8 -*-

import simple_draw as sd
import random
import time

sd.resolution = (800, 800)

default_color = sd.COLOR_RED
random_value = 50
triangle_start_draw_position_x = 100
triangle_start_draw_position_y = 100
square_start_draw_position_x = 700
square_start_draw_position_y = 700
pentagon_start_draw_position_x = 100
pentagon_start_draw_position_y = 600
hexagon_start_draw_position_x = 600
hexagon_start_draw_position_y = 100
triangle_start_draw_position = sd.get_point(triangle_start_draw_position_x, triangle_start_draw_position_y)
square_start_draw_position = sd.get_point(square_start_draw_position_x, square_start_draw_position_y)
pentagon_start_draw_position = sd.get_point(pentagon_start_draw_position_x, pentagon_start_draw_position_y)
hexagon_start_draw_position = sd.get_point(hexagon_start_draw_position_x, hexagon_start_draw_position_y)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
# start_draw_position, side_length, figure_color


def draw_triangle():

    # first_point_x, first_point_y, line_length
    def generate_point_list():
        point_list = [triangle_start_draw_position]
        second_point = sd.get_point(triangle_start_draw_position_x + random.choice((-random_value, random_value)),
                                    triangle_start_draw_position_y + random.choice((-random_value, random_value)))
        point_list.append(second_point)
        return point_list
    sd.lines(generate_point_list(), default_color, True)


draw_triangle()
sd.time.sleep(1)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
