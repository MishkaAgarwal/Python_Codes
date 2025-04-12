#Rock, Paper, and Scissors game program
print('========================')
print('Rock, Paper and Scissors')
print('========================')
import random
choices= ['Rock', 'Paper', 'Scissors']
repeat= int(input('How many rounds do you want to play the game for? '))
up=0
cp=0
for i in range(repeat):
    uc=input('Enter the move you want to play. Your options are Rock, Paper or Scissors. ')
    uc=uc.capitalize()
    if uc not in (choices):
        print('Invalid input. Please input Rock, paper or scissors ')
        continue
    else:
        pass
    cc= random.choice(choices)
    print("The computer's choice is:", cc)
    #pointing
    if uc==cc:
        print("It's a tie")
    else:
        if (uc=='Scissors' and cc=='Paper')or (uc=='Rock' and cc=='Scissors') or (uc=='Paper' and cc=='Rock'):
            print('You win a point!')
            up+=1
        else:
            print('The computer wins a point')
            cp+=1
#printing score and end messages
print('Your score is', up, 'points', "and the computer's score is", cp, 'points')
if up<cp:
    print('The computer wins')
elif up>cp:
    print('You win!')
elif up==cp:
    print('There is a tie')
print('You have reached the end of the game.')
print('Bye, and hope you enjoyed playing!')

