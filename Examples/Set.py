#!/usr/bin/env python3
# -*- coding: utf-8 -*-

cities = ['Санкт-Петербург', 'Хабаровск', 'Казань', 'Санкт-Петербург', 'Казань']
un_cities = set(cities)

if __name__ == '__main__':
    for city in un_cities:
        print("Один мой друг живёт в городе " + city)