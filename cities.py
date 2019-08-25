
import random

list_bot = ['ты', 'вы', 'компьютер', 'бот']
cities = ['москва', 'санкт-петербург', 'алматы', 'грозный', 'самара']

def last_letter(city):
    last = city[-1]
    if last in ['ь','ъ','ы']:
        last = city[-2]
    return last

def game():
    named_cities = []
    who = input('Кто начинает? Я или Вы? ').lower()
    if who in list_bot:
        bot_city = random.choice(cities)
        user_city = input(bot_city + ' ')
    else:
        user_city = input('Ваш вариант: ')

    while True:
        named_cities.append(user_city)
        last = last_letter(user_city)
        user_city = input(random.choice([word for word in cities if word.startswith(last)]) + ' ')
        if user_city.lower() in ['устал', 'хватит', 'стоп']:
            print('Спасибо за игру!')
            break
        elif user_city.lower() in named_cities:
            print('Этот город уже был!')
            continue

if __name__ == '__main__':
    game()