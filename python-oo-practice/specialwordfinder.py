"""Special word finder: A subclass of wordfinder that formats a more specific list"""
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
    This class functions similarly to the wordfinder class, but formats for use of the # and extra white lines

    >>> wordList = SpecialWordFinder("/home/kevin/springboard/SpringBoardAssignments/python-oo-practice/specialwords.txt")
    10 words read
    {'Veggies': ['kale', 'parsnips'], 'Fruits': ['apple', 'mango']}
    
    """
    def __init__(self, file):
        super().__init__(file)
        specialWords = self.format()
        print(specialWords)
        
    
    def format(self):
        categories = {}
        hashFlag = False
        
        for line in self.list:
            if len(line.strip()) > 0:
                if line[0] == "#":
                    currCategory = line[2:]
                    categories[currCategory] = []
                    hashFlag = True
                elif hashFlag:
                    categories[currCategory].append(line)
        
        return categories
            