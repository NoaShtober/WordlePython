from Printer import Printer, ColorfulPrinter, BlackAndWhitePrinter

class Game:
  def __init__(self, SelectedWord, PrintMethod):
    self.SelectedWord = SelectedWord.lower()
    self.PrintMethod = PrintMethod
   
  def turn(self, guess, WordLength):
      ResultsList = [0] * WordLength
      MatchingLettersList = [0] * 26
     
      for i in range(WordLength):
          CurrentLetter = guess[i]
          if self.SelectedWord[i] == CurrentLetter:
              ResultsList[i] = True
              MatchingLettersList[ord(CurrentLetter)-97] += 1
             
      for i in range(WordLength):
          CurrentLetter = guess[i]
          if self.SelectedWord[i] == CurrentLetter:
              MatchingLettersList[ord(CurrentLetter)-97] -= 1
          if CurrentLetter not in self.SelectedWord:
              ResultsList[i] = False
              continue
          elif self.SelectedWord[i] != CurrentLetter and guess[0:i+1].count(CurrentLetter) + MatchingLettersList[ord(CurrentLetter)-97] <= self.SelectedWord.count(CurrentLetter):
              ResultsList[i] = 'Place'
          elif ResultsList[i] == 0:
              ResultsList[i] = False
      return ResultsList
     
  def Printing(self, guess, ResultsList):
      if self.PrintMethod == 'colorful':
          colorful = ColorfulPrinter(guess, ResultsList)
          colorful.PrintResult()
      if self.PrintMethod == 'BlackAndWhite':
          BlackAndWhite = BlackAndWhitePrinter(guess, ResultsList)
          BlackAndWhite.PrintResult()
     
         
  def IsGuessCorrect(self,guess, WordLength):
      LengthOfVictory = 5
      ResultsList = self.turn(guess, WordLength)
      self.Printing(guess, ResultsList)
      return ResultsList.count(True) == LengthOfVictory
    
  def isWordNotValid(self, guess, WordLength):
      return len(guess) != WordLength or not guess.isalpha()
        
                  
  def FullGame(self, WordLength,NumberOfAllowedGuesses):
      for i in range(0, NumberOfAllowedGuesses):
          guess = input('Enter your guess: ')
          while self.isWordNotValid(guess, WordLength):
             guess = input('Enter your guess: ')
          lowerCaseGuess = guess.lower()
          Result = self.IsGuessCorrect(lowerCaseGuess, WordLength)
          if Result == True:
              print ('You Won!')
              return True
          elif Result == False and i == NumberOfAllowedGuesses - 1:
             print ('You Lost!')
             return True
      return True
