import random

easyTurn=10
hardTurn=5

def check(guess, answer,turns):
    '''This will return ur guess and turns left'''
    if guess>answer:
        print('TOO HIGH')
        return turns-1
    elif guess<answer:
        print('TOO Low')
        return turns-1
    else:
        print(f'you guessed it and the answer was {answer}')
        
def difficulty():
    level=input(r'Choice "easy" and "hard"')
    if level=='easy':
        return easyTurn
    if level=='hard':
        return hardTurn
def game():    
    answer=random.randint(1,100)
    print(answer) 

    print('Welcome to guessing game ')
    print('choice any number between 1 to 100\n\n')
    turns=difficulty()
    guess=0
    while answer!=guess:
        print(f'You have {turns} attempts')
        guess=int(input('Guess the number '))
        turns=check(guess, answer,turns)
        if turns==0:
            print('you run out of attempts')
            return 
game()        
