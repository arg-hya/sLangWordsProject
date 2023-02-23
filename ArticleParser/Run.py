from ArticleParser.ParseAndModify import ParseAndModify
from DBConnector.sLangDBs import Abbrebreations, SlangDB


def initialize():
    abr = Abbrebreations()
    abrDict = abr.getAbbDict()
    #abr.printDict()

    testSlangs = SlangDB()
    testSlangsDict = testSlangs.getSlangDict()
    #testSlangs.printDict()

    return abrDict, testSlangsDict

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # abr = initialize()
    #
    # print("Parsing and Modifying...")
    # print(type(abr))
    # ParseAndModify(abr)

    abrDict, testSlangsDict = initialize()
    print("Parsing and Modifying...")
    ParseAndModify(abrDict, testSlangsDict)

