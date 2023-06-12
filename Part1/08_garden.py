#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
print(garden_set, meadow_set)

# выведите на консоль те, которые растут и там и там
both_flowers = set()
for flower in garden_set:
    if flower in meadow_set:
        both_flowers.add(flower)
print(both_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden_flowers = set()
for flower in garden_set:
    if flower not in meadow_set:
        only_garden_flowers.add(flower)
print(only_garden_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow_set = set()
for flower in meadow_set:
    if flower not in garden_set:
        only_meadow_set.add(flower)
print(only_meadow_set)


