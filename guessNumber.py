import random

list_bot = ['ты', 'вы', 'компьютер', 'бот']

def gameGuessing():
    min = 0
    max = 101
    ready = input('Когда будете готовы, напишите: готов. ')
    if ready == 'готов':
        while min != max:
            rndGuess = random.randint(min, max)
            matching = input(str(rndGuess) + ' ')
            if matching == 'больше':
                min = rndGuess
            else if matching == 'меньше':
                max = rndGuess

    else:
        print('что-то пошло не так')

def gameCreating():
    
def game():
    player1 = input('Кто будет загадывать: я или Вы? ')
    if player1 in list_bot:
        gameGuessing()
    else:
        gameCreating()

game()