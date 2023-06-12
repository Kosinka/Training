#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
    'Kursk': (460, 460)
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distances = {}

for city in sites.keys():
    coordinates = sites[city]
    city_coordinate_x, city_coordinate_y = coordinates[0], coordinates[1]
    for cities in sites.keys():
        if city == cities:
            pass
        else:
            second_city_coordinates = sites[cities]
            second_city_coordinate_x, second_city_coordinate_y = second_city_coordinates[0], second_city_coordinates[1]
            distance_key = city + ' ' + cities
            distance = ((city_coordinate_x - second_city_coordinate_x) ** 2 + (city_coordinate_y - second_city_coordinate_y) ** 2) ** 0.5
            distances[distance_key] = distance

print(distances)
