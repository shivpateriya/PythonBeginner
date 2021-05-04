import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
user = int(input("What do you choose? FOR 'ROCK  0 ','PAPER 1 ','SCISSORS 2'\n").lower())


print(game[user])
Computer=random.choice([0,1,2])
print(game[Computer])
print('Computer choice:')
if user==0  and Computer==2:
    print('You win')
elif user==2 and Computer==0:
    print('you loose')
elif user==0 and Computer==1:
    print('you loose')
elif user==1 and Computer==0:
    print('you won')
elif user==1 and Computer==2:
    print('you loose')
elif user==2 and Computer==1:
    print('you  won')
elif user==Computer:
    print('Its draw')
else:
    print('Wrong input')
