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

sLangTags = {'vulgar', 'derogatory', 'slang', 'strong', 'strongly', 'internet'}
def getBestDefinedIndex(definations):
    best_index = 0
    max_score = 0
    for key in definations.keys():
        tags = definations[key][0][0]
        score = len([i for i in sLangTags if i in tags])
        if max_score < score :
            best_index = key
            max_score = score
    return best_index



parser = WiktionaryParser()
parser.set_default_language('english')
parser.exclude_part_of_speech('interjection')

def getDefinationfromWikiDictionary(sLangWord):
    word = parser.fetch(sLangWord)
    definations = {}
    count = 0

    if 0 == len(word):
        return ''

    if 0 == len(word[0]['definitions']):
        return ''

    for i in range(0,len(word)):
        for definitions in word[i]['definitions']:
            for text in definitions['text']:
                tags = getDefinationTags(text)
                defination = getDeinationsWithoutTags(text, tags)
                if len(tags) > 0 and defination:
                    definations[count] = (tags, defination)
                    count += 1

    #print(definations)
    if len(definations) == 0:
        return 'NOT_DEFINED_WIKI'

    bestIndex = getBestDefinedIndex(definations)
    return definations[bestIndex][1].split('\n')[0]