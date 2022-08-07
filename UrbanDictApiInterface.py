import json
import string

import requests
import re

validChars = set.union(set(string.ascii_lowercase), set(string.ascii_uppercase), \
                       set(string.digits), set(string.whitespace), {'.',':','%',',',';','!','\"','$','\''} )


class UrbanWord:
  def __init__(self, word, defination = '', example = '', score = 0):
    self.valid = False
    self.word = word
    self.defination = defination
    self.example = example
    self.score = score

  def print(self):
      print("Word : ", self.word)
      print("Defination : ", self.defination)
      print("Example : ", self.example)
      print("Score : ", self.score)

  def getExample(self):
      return self.example

  def getScore(self):
      return self.score

  def getUrbanWord(self):
      return self.word

  def getDefinition(self):
      return self.defination

  def setValid(self):
      self.valid = True

def replaceInvalidChars(text) :
    #print("Valid chars : ", validChars )
    for char in text:
        if char not in validChars :
            text = text.replace(char, "")
    return text

# Python program to find the largest
# number among the three numbers

def getWordWithBestScore(a, b, c):
    if (a.score >= b.score) and (a.score >= c.score):
        bestWord = a

    elif (b.score >= a.score) and (b.score >= c.score):
        bestWord = b
    else:
        bestWord = c

    return bestWord

def isFirstElemNotChar(inputString):
    return not inputString[0].isalpha()

def remove_all_extra_characters(string):
    if not string:
        return ""       #invalid string
    if True == isFirstElemNotChar(string):
        string = string[1:]
        string = remove_all_extra_characters(string)
    return string.strip()

def getResponseForWord(word, printResponse = False):
    response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")

    if True == printResponse :
        print(json.dumps(response.text, indent=4, sort_keys=True))

    return response.text

def getDefination(jsonData):
    defination = jsonData["definition"].split('\n')[0]
    defination = replaceInvalidChars(defination)
    #print(defination)
    return remove_all_extra_characters(defination)

def getMatchingLine(string, word):
    for line in string.split("\n"):
        if word in line:
            return line.strip()

    return string

def getExample(jsonData, word):
    example = getMatchingLine(jsonData["example"], word)
    example = replaceInvalidChars(example)
    #print(word, " Example : ", example)
    return remove_all_extra_characters(example)

def getDefinationDict(jsonData, bestDefIndex):
    data = jsonData["list"][bestDefIndex]
    #print(data)
    return data

def isValidUrbanWord(jsonData):
    count = len(jsonData["list"])
    if 0 == count :
        return False
    return True

def getHighestRatedDefination(word, jsonData):
    count = len(jsonData["list"])
    #print("Total number of definations : ", count)

    residualVote = 0
    bestDefIndex = 0

    for i in range(0,count):
        defDict = jsonData["list"][i] #gets defDict
        upVote = defDict["thumbs_up"] #gets number of UP Votes
        downVote = defDict["thumbs_down"]  # gets number of DOWN Votes

        diffVote = upVote - downVote

        if diffVote > residualVote :
            residualVote = diffVote
            bestDefIndex = i

    try :
        defDict = getDefinationDict(jsonData, bestDefIndex)
        definition = getDefination(defDict)  # definition of word
        example = getExample(defDict, word)  # example of word
    except Exception as ex:
        print("Exception caught : ", ex)
        print("Detailed logs,  Word : ", word, " defDict", json.dumps(defDict, indent=4, sort_keys=True))

    #print(json.dumps(defDict, indent=4, sort_keys=True))

    if not definition or not example :
        return UrbanWord(word)  #Invalid word, ignore it based on low score
    else :
        return UrbanWord(word, definition, example, residualVote)

def getWordParameters(word):
    data = json.loads(getResponseForWord(word)) #gets defination and converts to JSON

    if True == isValidUrbanWord(data) :
        return getHighestRatedDefination(word, data)
    else:
        return UrbanWord(word)

def getWord(word):
    wordObj_ori = getWordParameters(word)
    #wordObj_ori.print()

    # #Uppercase
    # wordObj_upper = getWordParameters(word.upper())
    # #wordObj_upper.print()
    #
    # #Lowercase
    # wordObj_lower = getWordParameters(word.lower())
    # #wordObj_lower.print()
    #
    # #Get the one with the best score
    # wordObj = getWordWithBestScore(wordObj_ori, wordObj_upper, wordObj_lower)
    # #wordObj.print()

    return wordObj_ori

def getExampleText(word):
    return getWord(word).example



#getWord("assclown")
