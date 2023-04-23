

import random
import string
from Game import Game


#words = ['hello', 'crate', 'shade', 'resin', 'alert', 'media', 'flood', 'award', 'bully', 'orate', 'legal', 'boost']
with open("words.txt") as file_in:
    words = []
    for line in file_in:
        words.append(line)
file_in.close()

ContinueGame = 'yes'

WordLength = 5
NumberOfAllowedGuesses = 5

print ('Welcome to Wordle!')
printingMethod = input("Please select printing method: colorful/BlackAndWhite ")
while ContinueGame == 'yes':
    SelectedWord = random.choice(words)
    print(SelectedWord)
    game1 = Game(SelectedWord, printingMethod)
    game1.FullGame(WordLength,NumberOfAllowedGuesses)
    ContinueGame = input('Would you like to continue? (yes/no) ')
