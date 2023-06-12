#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

duration = 0.0
for song in violator_songs_list:
    if song[0] == 'Enjoy the Silence':
        duration += song[1]
    elif song[0] == 'Halo':
        duration += song[1]
    elif song[0] == 'Clean':
        duration += song[1]
print('Три песни звучат: ' + str(round(duration, 2)) + ' минут.')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

duration = 0.0
for song in violator_songs_dict.keys():
    if song == 'Sweetest Perfection':
        duration += violator_songs_dict['Sweetest Perfection']
    elif song == 'Policy of Truth':
        duration += violator_songs_dict['Policy of Truth']
    elif song == 'Blue Dress':
        duration += violator_songs_dict['Blue Dress']
print('А другие три песни звучат: ' + str(round(duration, 2)) + ' минут.')
