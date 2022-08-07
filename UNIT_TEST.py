import string

from FilterPipeline import applyAdvancedFilters, passFilterPipelineAndGetDefinition
from WordListCrawler import fromParticularPageTest

def nerTest():
    word = "abrahamming"
    # wordObj = getWord(word)
    # exampleText = wordObj.getExample()

    print(applyAdvancedFilters(word))

    # print(applyStanfordNERonExample(exampleText, wordObj.getUrbanWord(), True))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting...")
    file = "debug.txt"
    f = open(file, "w")
    pageNum = 1
    for entry_set in fromParticularPageTest():
        for word in entry_set:
            sLangWord, definition = passFilterPipelineAndGetDefinition(word)
            if sLangWord:
                print("Keeping this word : ", sLangWord)
                f.write(sLangWord + ' , ' + definition + '\n')
        # if pageNum == 10:
        #    break
        pageNum += 1
    f.close()
