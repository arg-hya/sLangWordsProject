from UrbanDictApiInterface import getWord
from WiktionaryInterface import getDefinationfromWikiDictionary

#Get the definitions from Urban Dict and Wiki Dict
def getDifinition(word) :
    wordObj = getWord(word)             #Urban Dict API
    wordScore = wordObj.getScore()

    #get definition from Wiktionary
    defination_WIKI = getDefinationfromWikiDictionary(wordObj.word)
    #get definition from Urban Dictionary
    defination_UB = wordObj.getDefinition()

    if defination_WIKI :
        #print("Def from Wiki : ", word, " : ", defination_WIKI)
        return defination_WIKI

    else :
        #print("Def from UB : ", word, " : ", defination_UB)
        return defination_UB
