import random

list_bot = ['ты', 'вы', 'компьютер', 'бот']
cities = ['москва', 'санкт-петербург', 'алматы', 'грозный', 'самара']

def last_letter(city):
    last = city[-1]
    if last in ['ь','ъ','ы']:
        last = city[-2]
    return last


def game():
    who = input('Кто будет загадывать? Я или Вы? ').lower()
    if who in list_bot:
        bot_city = random.choice(cities)
        user_city = input(bot_city + ' ')
    else:
        user_city = input('Загадывайте: ')

    last = last_letter(user_city)
    print([word for word in cities if word.startswith(last)])

game()