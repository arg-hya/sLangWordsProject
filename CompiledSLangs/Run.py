# Press the green button in the gutter to run the script.
import csv

from CompiledSLangs.DefinitionExtractor import getDifinition
from DBConnector.DataAccessInterface import writeSlangAndDefinitionAndSynonym
from SynonymExtraction.SynonymExtrator_1000 import  getSynonym


def createMergedDB():
    SlangDBs = []
    rootDir = "Additional_UrbanWordsList"
    slangDBFilePaths = [rootDir + "/bad_phrases.txt",
                        rootDir + "/bad_words.txt",
                        rootDir + "/common_curse_words.txt",
                        rootDir + "/Google_WDYL_Project.txt",
                        rootDir + "/profanity_wordlist.txt",
                        rootDir + "/profanity-filter.txt",
                        rootDir + "/Shutterstock.txt"
                        ]
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

def createMergedDBwithSynonyms() :
    slang_dict = readMergedDBbyLine()
    #print(slang_dict)

    for key in slang_dict.keys() :
        print(key, " : ", slang_dict[key])
        synonym = getSynonym(slang_dict[key])
        #input("Press Enter to continue...")

        #Insert in DB
        writeSlangAndDefinitionAndSynonym(key, slang_dict[key], synonym)

if __name__ == '__main__':

    ##Create the merged DB
    ##createMergedDB()

    ##Clean Merged DB
    #ModifyMergedDB() #Nothing done yet

    #Get Synonyms
    createMergedDBwithSynonyms()





