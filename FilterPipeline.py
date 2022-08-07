from NERFilter import applyStanfordNERonExample
from UrbanDictApiInterface import getWord
from WiktionaryInterface import getDefinationfromWikiDictionary

slangWord = ['','']

def allCharactersSame(s):
    if not s:
        return True

    #store first character
    s1 = {s[0]}

    # Insert characters in
    # the set
    for i in range(1, len(s)):
        s1.add(s[i])

    # If all characters are same
    # Size of set will always be 1
    if (len(s1) == 1):
        return True
    else:
        return False

def allCharactersSameSubstring(s):
    mid = int(len(s)/2)
    ss = s[0:mid]
    return allCharactersSame(ss)

def applyBasicFilters(word):

    if False == word.isalnum():
        return False
    if word == "":
        return False
    if len(word) > 15:
        return False
    if len(word) < 3:
        return False
    if allCharactersSame(word.lower()):
        return False
    if allCharactersSameSubstring(word.lower()):
        return False

    return True

def modifyWord(word):
    slangWord[0] = word

def setDefinition(wordObj):

    #get definition from Wiktionary
    defination_WIKI = getDefinationfromWikiDictionary(wordObj.word)
    #get definition from Urban Dictionary
    defination_UB = wordObj.getDefinition()

    if defination_WIKI :
        slangWord[1] = defination_WIKI
        print("Def from Wiki : ", defination_WIKI)
    else :
        slangWord[1] = defination_UB
        print("Def from UB : ", defination_UB)

def applyAdvancedFilters(word):
    wordObj = getWord(word)
    wordScore = wordObj.getScore()

    if wordScore < 200 :
        print("Low Score: ", word)
        return False

    print("Applying advanced filters for : ", wordObj.getUrbanWord())
    exampleText = wordObj.getExample()
    if False == applyStanfordNERonExample(exampleText, wordObj.getUrbanWord(), False):
        return False

    #Mark the wordObj as valid
    wordObj.setValid()
    #print("Keeping this word: ", word)
    setDefinition(wordObj)

    return True

def passFilterPipelineAndGetDefinition(word):
    #reseting tuple for new word
    slangWord[0] = ''
    slangWord[1] = ''

    if True == applyBasicFilters(word):
        if True == applyAdvancedFilters(word):
            modifyWord(word)
            print(slangWord)
            return tuple(slangWord)

    return tuple(slangWord)