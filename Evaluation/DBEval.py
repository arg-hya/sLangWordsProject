# Press the green button in the gutter to run the script.
from ArticleParser.ArticleParseReplace import ParserReplacer
from nltk.translate.bleu_score import sentence_bleu
import datetime
import pandas as pd

def calculateBLEU():
    inputFilePath = "../ArticleParser/DemoOutput.txt"
    with open(inputFilePath) as file:
        lines = [line.rstrip() for line in file]

    lines = [line for line in lines if len(line) != 0]

    inputFilePath_1 = "../ArticleParser/DemoOutput_para.txt"
    with open(inputFilePath_1) as file:
        lines_can = [line.rstrip() for line in file]

    lines_can = [line for line in lines_can if len(line) != 0]

    print(lines)
    for ind in range(0,len(lines)):
        print(ind)
        reference = lines[ind].split()
        candidate = lines_can[ind].split()
        print("reference : ", reference)
        print('BLEU score -> {}'.format(sentence_bleu(reference, candidate)))

def getTimeComsumption(df_cd):
    start = datetime.datetime.now()
    parserReplacer = ParserReplacer(replacer=True)
    count = 0
    print(count)
    print("Starting...")
    for index, row in df_cd.iterrows():
        #print("itr...")
        text = row['comment_text']
        definition = row['obscene']
        #print(text)
        if parserReplacer.hasSlang(text) == True:
            count = count + 1
            #print(count)
        if count == 1:
            lap1 = start - datetime.datetime.now()
            print("lap1 : ", lap1.total_seconds() * 1000)
        if count == 10:
            lap2 = start - datetime.datetime.now()
            print("lap2 : ", lap2.total_seconds() * 1000)
        if count == 100:
            lap3 = start - datetime.datetime.now()
            print("lap3 : ", lap3.total_seconds() * 1000)
            break


def testResult():
    parserReplacer = ParserReplacer(replacer=False)
    text =  " :Dear god this site is horrible."
    print(parserReplacer.hasSlang(text))

def testCSV(df_cd):
    for index, row in df_cd.iterrows():
        # print(index)
        text = row['comment_text']
        definition = row['obscene']
        if definition == 1:
            print("aaa ", text)
        if index == 1000:
            break



def getAccuracy(df_cd):
    parserReplacer = ParserReplacer(replacer=False)

    TP = 0
    FP = 0
    TN = 0
    FN = 0
    acc = 0
    for index, row in df_cd.iterrows():
        # print(index)
        text = row['comment_text']
        definition = row['obscene']
        res = 0
        if parserReplacer.hasSlang(text) == True:
            res = 1
        # if definition == 1:
        #     print("aaa ", res)
        if res == definition:
            acc = acc + 1
        if res == 1:
            if res == definition:
                TP = TP + 1
            else:
                #print("aaa ", text)
                FP = FP + 1
        if res == 0:
            if res == definition:
                TN = TN + 1
            else:
                FN = FN + 1
        # else :
        #     print(definition, " : ", text )
        if index % 1000 == 0:
            print(index)
        if index == 5000:
            break

    total_points = len(df_cd.index)
    print("total_points : ", total_points)
    #acc = acc / total_points
    print("Accuracy : ", acc)
    print("TP ", TP)
    print("FP ", FP)
    presision = TP / (TP + FP)
    recall = TP / (TP + FN)
    print("presision : ", presision)
    print("recall : ", recall)
    f1_score = 2 * ((presision * recall) / (presision + recall))
    print("F1 score : ", f1_score)

if __name__ == '__main__':
    filepath_data = r"C:\Users\kundu\Desktop\Research\My projects\Slang\jigsaw-toxic-comment-classification-challenge\test.csv\test.csv"
    df1 = pd.read_csv(filepath_data, sep=",", encoding='mac_roman')
    print(df1.columns)

    filepath_data_labels = r"C:\Users\kundu\Desktop\Research\My projects\Slang\jigsaw-toxic-comment-classification-challenge\test.csv\test_labels.csv"
    df1_labels = pd.read_csv(filepath_data_labels, sep=",", encoding='mac_roman')
    print(df1_labels.columns)

    df_cd = pd.merge(df1, df1_labels, how='inner', on='id')
    #print(df_cd.columns)
    df_cd = df_cd[['comment_text', 'obscene']]
    #print(df_cd.head())
    #df_cd = df_cd[~df_cd['obscene'] == -1]
    df_cd = df_cd[df_cd['obscene'] != -1]
    print(df_cd.head())
    df_cd = df_cd.reset_index(drop=True)

    #getAccuracy(df_cd)
    #getTimeComsumption(df_cd)
    #testResult()
    #testCSV(df_cd)
    calculateBLEU()

