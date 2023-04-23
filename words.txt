
from abc import ABC, abstractmethod

class Printer(ABC):
   
    def __init__(self, guess, ResultList):
        self.guess = guess
        self.ResultList = ResultList
   
   @abstractmethod
    def PrintResult(self):
        pass
   

class ColorfulPrinter(Printer):
   
    def PrintResult(self):
        for i in range(0, len(self.ResultList)):
            if (self.ResultList[i] == True):
                print ('\033[32m' + str(self.guess[i]), end = "\033[0m")
            if (self.ResultList[i] == False):
                print ('\033[31m' + str(self.guess[i]), end = "\033[0m")
            if (self.ResultList[i] == 'Place'):
                print ('\033[33m' + str(self.guess[i]), end = "\033[0m")
        print('\n')
       

class BlackAndWhitePrinter(Printer):
   
    def PrintResult(self):
        for i in range(0, len(self.ResultList)):
            if (self.ResultList[i] == True):
                print ("T", end = "")
            if (self.ResultList[i] == False):
                print ("F", end = "")
            if (self.ResultList[i] == 'Place'):
                print ("P", end = "")
               
        print('\n')
