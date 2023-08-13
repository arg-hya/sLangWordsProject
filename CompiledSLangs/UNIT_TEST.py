import csv

from DBConnector.DataAccessInterface import isWordSlang, getSlangSynonym
from WiktionaryInterface import getDefinationfromWikiDictionary

def WIKI_Definition_Test():
    word = 'Balls'
    print("Running UNIT TEST...")
    defination_WIKI = getDefinationfromWikiDictionary(word)
    print("Def from Wiki : ", word, " : ", defination_WIKI)

#Read the merged DB
def readMergedDB():
    abb_dict = {}
    with open('Additional_UrbanWordsList/MergedSlangsDB_definition.txt', mode='r', encoding="utf-8") as infile:
        reader = csv.reader(infile)
        abb_dict = {rows[0]: rows[1] for rows in reader}
    print(abb_dict['5h1t'])

def testSlangs():
    word = "Hello"
    while word != 'quit':
        word = input("Please enter text, or enter 'quit': ")
        if isWordSlang(word) == True:
            print("Word : ", word, "is Slang")
            print(word, " : ", getSlangSynonym(word))
        else:
            print("Word : ", word, "is NOT Slang")

if __name__ == '__main__':
    testSlangs()