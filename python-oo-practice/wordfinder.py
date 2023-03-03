"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """A class that returns a random word from a file

    "https://stackoverflow.com/questions/16341484/doctest-for-a-function-using-a-randomly-generated-variable"
    There is an explanation how .seed can be used from random to set a testable random value
    

    >>> random.seed(1)
    
    >>> wordFinder = WordFinder("/home/kevin/springboard/SpringBoardAssignments/python-oo-practice/words.txt")
    235886 words read

    >>> wordFinder.random()
    'choler'

    >>> wordFinder.random()
    'pneumodynamics'

    >>> wordFinder.random()
    'unrulableness'

    """

    def __init__(self, filePath):
        self.list = self.parseList(filePath)
        

    """ parses file and returns a list of words"""
    def parseList(self, filePath):
        file = open(filePath)
        wordList = []
        count = 0
        for line in file:
            parsedWord = line.replace("\n" , "")
            wordList.append(parsedWord)
            count+=1
        
        print(f"{count} words read")
        return wordList

    """ takes a random word out of the list"""
    def random(self):
        randomIndex = random.randint(0, len(self.list)-1)
        return self.list[randomIndex]
