from DBConnector.DataBaseCreator import DBCreator
from DBConnector.DataBaseReader import DBReader


#########Creator API############
def writeSlang(word):
    word = word.strip()
    DBCreator.getInstance().insert_SlangAndDef(word, "NULL")

def writeSlangAndDefinition(word, definition):
    word = word.strip()
    DBCreator.getInstance().insert_SlangAndDef(word, definition)

def writeSlangAndDefinitionAndSynonym(word, definition, synonym):
    word = word.strip()
    DBCreator.getInstance().insert_SlangAndDefAndSyn(word, definition, synonym)

def writeSlangAndSynonym(word, synonym):
    word = word.strip()
    DBCreator.getInstance().update_synonym(word, synonym)

def deleteSlang(word):
    word = word.strip()
    DBCreator.getInstance().delete_task(word)

#########Reader API############
def isWordSlang(word):
    word = word.strip()
    return DBReader.getInstance().is_slang(word)

def getSlangDefinition(word):
    word = word.strip()
    return DBReader.getInstance().select_definition_by_slang(word)[0][0]

def getSlangSynonym(word):
    word = word.strip()
    return DBReader.getInstance().select_synonym_by_slang(word)[0][0]

def debugPrintDB():
    DBReader.getInstance().debug_printDB()

# #DBReader.getInstance().select_all_tasks()
# writeSlangAndDefinitionAndSynonym('slang40', 'def40', 'syn40')
# print(isWordSlang('slang40'))
# print(getSlangDefinition('slang40'))
# print(isWordSlang('slang2'))
# print(getSlangDefinition('slang2'))

# writeSlangAndDefinitionAndSynonym('slang4', 'def4', 'syn4')
# writeSlangAndDefinitionAndSynonym('slang2', 'def5', 'syn5')
# writeSlangAndDefinitionAndSynonym('slang6', 'def6', 'syn6')
#
# print(isWordSlang('slang26'))
# print(isWordSlang('slang6'))
# print(getSlangDefinition('slang6'))
# print(getSlangSynonym('slang6'))
# writeSlangAndDefinitionAndSynonym('slang6', 'def_new', 'syn_new')
# print(isWordSlang('slang6'))
# print(getSlangDefinition('slang6'))
# print(getSlangSynonym('slang6'))

#debugPrintDB()


