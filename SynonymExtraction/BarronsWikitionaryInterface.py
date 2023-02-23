from wiktionaryparser import WiktionaryParser
import re

def getDeinationsWithoutTags(text, tags):
    for tag in tags:
        if tag in text:
            text = text.replace(tag, '')
    return text

def getDefinationTags(text):
    # Extract substrings between brackets
    # Using regex
    tags = re.findall(r'\(.*?\)', text)
    return tags

sLangTags = {'vulgar', 'derogatory', 'slang', 'strong', 'strongly'}
def getBestDefinedIndex(definations):
    best_index = 0
    max_score = 0
    for key in definations.keys():
        #print(definations[key])
        score = len(definations[key])
        if max_score < score :
            best_index = key
            max_score = score
    return best_index



parser = WiktionaryParser()
#parser.set_default_language('english')
#parser.exclude_part_of_speech('interjection')

def getDefinationfromWikiDictionary(sLangWord):
    #print('sLangWord : ', sLangWord)
    word = parser.fetch(sLangWord)
    definations = {}
    count = 0

    #print(word)

    if 0 == len(word):
        return ''

    if 0 == len(word[0]['definitions']):
        return ''

    for i in range(0,len(word)):
        for definitions in word[i]['definitions']:
            #print("definitions : ", definitions)
            for text in definitions['text']:
                tags = getDefinationTags(text)
                defination = getDeinationsWithoutTags(text, tags)
                if defination :
                    #print(tags, " :: ", defination)
                    definations[count] = defination
                    count += 1

    #print(definations)

    bestIndex = getBestDefinedIndex(definations)
    #print(sLangWord , " :: ", definations[bestIndex])
    return definations[bestIndex].split('.')[0]
