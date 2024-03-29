# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

list_bot = ['ты', 'вы', 'компьютер', 'бот']
got_it = ['верно', 'да', 'правильно']

def gameGuessing():
    min = 0
    max = 101
    input('Когда будете готовы, нажмите Enter. ')
    try:
        while True:
            rndGuess = random.randint(min, max)
            matching = input(str(rndGuess) + ' ').lower()
            if matching == 'больше':
                min = rndGuess + 1
            elif matching == 'меньше':
                max = rndGuess - 1
            elif matching in got_it:
                print('Ура!')
                break
    except:
        print('Извините, что-то пошло не так.')

def gameCreating():
    right_number = random.randint(0, 101)
    print('Я загадал.')
    while True:
        user_number = int(input('Ваш вариант: '))
        if user_number > right_number:
            print('меньше')
        elif user_number < right_number:
            print('больше')
        elif user_number == right_number:
            print('Вы угадали!')
            break

def main():
    player1 = input('Кто будет загадывать: я или Вы? ')
    if player1.lower() in list_bot:
        gameCreating()
    else:
        gameGuessing()

if __name__ == '__main__':
    main()