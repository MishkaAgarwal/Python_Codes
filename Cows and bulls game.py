#Cows and bulls game
print('='*21)
print('   Cows and bulls!   ')
print('='*21)
import random
words= ["bear", "zinc", "jinx", "blue", "cake", "fish", "gold", "love", "snow", "pink", 'huge', "wind", "star", "myth", "rain", "fire", "milk", "time", "plan", "quiz", "like", "cyan", 'hate', 'live', 'wave']
word= random.choice(words)
guess= ' '
c= ''
turns= 0
for y in range(100):
    guess= input('Enter a 4-letter word which which you think could be the main word ')
    guess= guess.lower()
    if len(guess)!=4:
        print('Input not accepted. Breaking the loop and exitting the game')
        break
    else:
        bulls= 0
        cows= 0
        for i in range(4):
            if word[i]==guess[i]:
                bulls= bulls +1
        for j in range(4):
            if guess[j]!= word[j] and guess[j] in word:
                cows= cows +1
        print('The guessed word has', cows, 'cows and', bulls, 'bulls')
        turns= turns+1
        if bulls==4:
            print('You have guessed the word correctly!')
            print('You have taken', turns, 'turns to guess the word')
            break

