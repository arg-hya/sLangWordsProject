# Press the green button in the gutter to run the script.
import csv
import os
import re
from pathlib import Path

from CompiledSLangs.DefinitionExtractor import getDifinition
from DBConnector.DataAccessInterface import writeSlangAndDefinitionAndSynonym
#from SynonymExtraction.SynonymExtrator_1000 import  getSynonym
from SynonymExtraction.SynonymExtractor_WordNet import getSynonym
import pandas as pd

import enchant
d = enchant.Dict("en_US")

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabets_sample = ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rootDir = "Additional_UrbanWordsList"
slangDBFilePaths = [rootDir + "/bad_phrases.txt",
                    rootDir + "/bad_words.txt",
                    rootDir + "/common_curse_words.txt",
                    rootDir + "/Google_WDYL_Project.txt",
                    rootDir + "/profanity_wordlist.txt",
                    rootDir + "/profanity-filter.txt",
                    rootDir + "/Shutterstock.txt"
                    ]

def addMissedCommonWords():
    infile = open(slangDBFilePaths[3], mode='r', encoding="utf-8")
    list_infile = list(infile)
    for k in range(0, len(list_infile)):
        list_infile[k] = list_infile[k].strip()

    for item in list_infile:
        # Trimm the strings
        item = item.strip()

        # if 20 == count :
        #     break
        # else :
        #     count = count + 1

        definition = getDifinition(item)
        if 'NOT_DEFINED_WIKI' == definition or \
                0 == len(definition) or \
                item == definition:
            continue

        # Trimm the strings
        definition = definition.strip()
        print(item, " : ", definition)
        putInDB(item, definition)

def createMergedDB():
    SlangDBs = []
    #Read and Merge all the datasets
    print("Read and Merge all the datasets...")
    print(slangDBFilePaths)
    sum = 0
    for i in range(0,len(slangDBFilePaths)) :
        print("Loading TestSlang Database :: ", slangDBFilePaths[i])
        infile = open(slangDBFilePaths[i], mode='r', encoding="utf-8")
        list_infile = list(infile)
        for k in range(0, len(list_infile)):
            list_infile[k] = list_infile[k].strip()
        SlangDBs.append(list_infile)
        sum = sum + len(SlangDBs[i])
        print("Length of ", slangDBFilePaths[i], ' :: ', len(SlangDBs[i]))

    print("Merging the DBs...")
    combinedDB = []
    for i in range(0,len(SlangDBs)):
        combinedDB = list(set(combinedDB + SlangDBs[i]))

    for i in range(0, len(combinedDB)):
        combinedDB[i] = combinedDB[i].strip()
    combinedDB.sort()

    print("Length of all words :: ", sum)
    print("Length of merged DB :: ", len(combinedDB))

    print(combinedDB)
    # open file in write mode
    with open(rootDir + '/MergedSlangs_WordsOnly.txt', 'w', encoding="utf-8") as fp:
        for item in combinedDB:
            # write each item on a new line
            fp.write("%s\n" % item)

    #GetDefinitions
    count = 0
    combinedDBDifinition = {}
    for item in combinedDB:
        # Trimm the strings
        item = item.strip()

        # if 20 == count :
        #     break
        # else :
        #     count = count + 1

        definition = getDifinition(item)
        if 'NOT_DEFINED_WIKI' == definition or \
                0 == len(definition) or \
                item == definition :
            continue

        # Trimm the strings
        definition = definition.strip()
        combinedDBDifinition[item] = definition
        print(item , " : ", combinedDBDifinition[item])

    #Write merged Dict in file
    # open file in write mode
    with open(rootDir + '/MergedSlangsDB_definition.txt', 'w', encoding="utf-8") as fp:
        for key in combinedDBDifinition:
            # write each item on a new line
            fp.write("%s,%s\n" % (key, combinedDBDifinition[key]))

#Read the merged DB
def readMergedDBbyLine():
    slang_dict = {}
    # removing the new line characters
    with open('Additional_UrbanWordsList/MergedSlangsDB_definition.txt', mode='r', encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]

    for line in lines :
        word, definition = line.split(',', 1)
        slang_dict[word] = definition
        #print(word, " : ", definition)
    return slang_dict

#Read the merged DB
def readMergedDB():
    slang_dict = {}
    with open('Additional_UrbanWordsList/MergedSlangsDB_definition.txt', mode='r', encoding="utf-8") as infile:
        reader = csv.reader(infile)
        slang_dict = {rows[0]: rows[1] for rows in reader}
    #print(slang_dict)
    return slang_dict

#Clean Merged DB
def ModifyMergedDB():
    slang_dict = readMergedDBbyLine()

    print(slang_dict)

def putInDB(word, definition, abbs = False):
    word = word.lower()
    synonym = definition
    if abbs == False :
        synonym = getSynonym(definition)
    # Insert in DB
    print(word, " :syn: ", synonym)
    writeSlangAndDefinitionAndSynonym(word, definition, synonym)

def isCommonWord(word):
    word = word.lower()
    return d.check(word)

def createMergedDBwithSynonyms() :
    slang_dict = readMergedDBbyLine()
    #print(slang_dict)

    for key in slang_dict.keys() :
        if isCommonWord(key) :      #Apply english language words filter
            print("Common word : ", key)
            continue
        print(key, " : ", slang_dict[key])
        putInDB(key, slang_dict[key])

    ##Take care of missed words
    #addMissedCommonWords()

def executeCompiledSlangs():
    #Create the merged DB
    #createMergedDB()

    #Clean Merged DB
    #ModifyMergedDB() #Nothing done yet

    #Get Synonyms
    createMergedDBwithSynonyms()

def executeAbbsSlangs():
    filepath_abbs = "../ArticleParser/AllAbbreviationsData.csv"
    df1 = pd.read_csv(filepath_abbs, sep=",", encoding='mac_roman')
    for index, row in df1.iterrows():
        word = row[0]
        definition = row[1]
        putInDB(word, definition, abbs = True)

def excuteUBslangs():
    for alphabet in alphabets_sample:
        dirpath = "../data/" + alphabet
        # iterate over files in
        # that directory
        files = Path(dirpath).glob('*')
        for file in files:
            print("Processing file : ", file)
            with open(file, 'r') as f:
                for line in f:
                    word = line.split(" ", 1)[0]
                    if isCommonWord(word):  # Apply english language words filter
                        print("Common word : ", word)
                        continue
                    definition = line.split(" ", 1)[1:][0]
                    definition = re.sub('[:;,!@#$]', '', definition)
                    #print(word, " : ", definition)
                    putInDB(word, definition)
            print("Processed file : ", file)


def testCreateDB():
    filepath_abbs = "../CompiledSLangs/Additional_UrbanWordsList/test_list.csv"
    df1 = pd.read_csv(filepath_abbs, sep=",", encoding='mac_roman')
    for index, row in df1.iterrows():
        word = row[0]
        definition = row[1]
        print(word, " : ", definition)
        putInDB(word, definition)

if __name__ == '__main__':

    # #Test creation of DB
    # testCreateDB()

    # #Add the abbreviations
    # print("Adding abbreviations to the database...")
    # executeAbbsSlangs()
    # #Add the slangs form other sources
    # print("Adding compiled slangs to the database...")
    # executeCompiledSlangs()
    # #Add the MissedCommonWords
    # print("Adding MissedCommonWords to the database...")
    # addMissedCommonWords()
    #Add the slangs from UB
    print("Adding UB slangs to the database...")
    excuteUBslangs()











