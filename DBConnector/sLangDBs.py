import numpy as np
import csv


class SlangDB:
    def __init__(self):
        self.filepath = r'D:\DarkWebResearch\sLang\archive\urban-dictionary-word-list-master\urban-dictionary-word-list-master\Additional_UrbanWordsList\test_list.csv'

    def __init__(self, filepath_custom):
        self.filepath = filepath_custom

    def getSlangDict_fromCSV(self):
        print("Loading TestSlang Database...")
        with open(self.filepath, mode='r', encoding="utf-8") as infile:
            self.reader = csv.reader(infile)
            self.abb_dict = {rows[0]: rows[1] for rows in self.reader}

        return self.abb_dict

    # Read the merged DB
    def getSlangDict(self):
        self.abb_dict = {}
        print("Loading TestSlang Database...")
        # removing the new line characters
        with open(self.filepath, mode='r', encoding="utf-8") as f:
            lines = [line.rstrip() for line in f]

        for line in lines:
            word, definition = line.split(',', 1)
            self.abb_dict[word] = definition
        return self.abb_dict

    def printDict(self):
        print("Slang Dict")
        #print(self.abb_dict)
        print("Length of Dict : ", len(self.abb_dict))
        print(type(self.abb_dict))


class Abbrebreations:
    def mergeDicts(self, firstDict, secondDict):
        res = {**firstDict, **secondDict}
        return res
    def __init__(self):
        self.filepath = r'D:\DarkWebResearch\sLang\archive\urban-dictionary-word-list-master\urban-dictionary-word-list-master\data\Abbrebreations\abbrevations_dictionary.npy'
        self.filepath_second = r'D:\DarkWebResearch\sLang\archive\urban-dictionary-word-list-master\urban-dictionary-word-list-master\data\Abbrebreations\abbreviations.csv'

    def getAbbDict(self):
        print("Loading Abbrebreations Database...")
        self.data = np.load(self.filepath, allow_pickle ='TRUE')
        self.abb_dict_first = self.data.item()

        with open(self.filepath_second, mode='r', encoding="utf-8") as infile:
            self.reader = csv.reader(infile)
            self.abb_dict_second = {rows[0]: rows[1] for rows in self.reader}

        self.abb_dict = self.mergeDicts(self.abb_dict_first, self.abb_dict_second)

        new_path = open("../ArticleParser/AllAbbreviationsData.csv", "w")
        z = csv.writer(new_path)
        for new_k, new_v in self.abb_dict.items():
            z.writerow([new_k, new_v])
        new_path.close()


        return self.abb_dict

    def printDict(self):
        print("Abbrebreations Dict")
        print(self.abb_dict_first)
        print(self.abb_dict_second)
        print(self.abb_dict)
        print(len(self.abb_dict_first))
        print(len(self.abb_dict_second))
        print(len(self.abb_dict))
        print(type(self.abb_dict))
