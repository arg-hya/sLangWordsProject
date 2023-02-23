import numpy as np
import collections
from sentence_transformers import SentenceTransformer
from DBConnector.sLangDBs import SlangDB
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('distilbert-base-nli-mean-tokens')

def get_cosine_similarity(feature_vec_1, feature_vec_2):
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]

def loadSlangDBwithDef():
    filepath = r'C:\Users\User\PycharmProjects\sLangDB\CompiledSLangs\Additional_UrbanWordsList\MergedSlangsDB_definition.txt'
    testSlangs = SlangDB(filepath)
    testSlangsDict = testSlangs.getSlangDict()
    #testSlangs.printDict()
    return testSlangsDict

def createWordEmbeddings(slangDict) :
    slangDB_embedd = {}
    keys = np.array(list(slangDict.keys()))
    values = np.array(list(slangDict.values()))

    text_data = values

    embeddings = model.encode(text_data, show_progress_bar=True)
    embed_data = embeddings

    X = np.array(embed_data)

    np.save(r'C:\Users\User\PycharmProjects\sLangDB\CompiledSLangs\Additional_UrbanWordsList\MergedSlangsDB_embeddings.npy', X)


def getSimilarSlangs(initialSlangDef, testSlangsDict) :
    print("Embedding test slan def...")
    X = np.array([initialSlangDef])
    text_data = X
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    embeddings = model.encode(text_data, show_progress_bar=True)

    embed_data = embeddings

    X = np.array(embed_data)

    all_embeddings = np.load(r'C:\Users\User\PycharmProjects\sLangDB\CompiledSLangs\Additional_UrbanWordsList\MergedSlangsDB_embeddings.npy')
    best_score = 0
    best_index = 0
    index = 0
    scores = {}
    print("Getting similar slangs...")
    for word in all_embeddings:
        score = get_cosine_similarity(X, word)
        scores[score] = index
        if best_score < score:
            best_score = score
            best_index = index
        index += 1

    # creating a data frame
    print('best_index : ', best_index)
    print(list(testSlangsDict.keys())[best_index])
    print(list(testSlangsDict.values())[best_index])


    sorted_score = collections.OrderedDict(sorted(scores.items(), reverse=True))

    count = 0
    for k, index in sorted_score.items():
        count += 1
        if 5 == count:
            break
        print("-------------Recommendation---------- :: ", count)
        print(list(testSlangsDict.keys())[index])
        print(list(testSlangsDict.values())[index])


#https://www.dhs.state.il.us/OneNetLibrary/27897/documents/Initiatives/HumanTrafficking/Human-Trafficking-Glossary-of-Terms.pdf
def processHumanTraffickingSlangs() :

    testDef = "Having sex with many people"
    #Load DB
    testSlangsDict = loadSlangDBwithDef()

    # #Create Word Embeddings
    # createWordEmbeddings(testSlangsDict)

    #Read Word Embeddings
    getSimilarSlangs(testDef, testSlangsDict)




