# import pandas module
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import collections

from sklearn.metrics.pairwise import cosine_similarity

def get_cosine_similarity(feature_vec_1, feature_vec_2):
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]

print("Loading Barron's 1000 word databse embedding...")
all_embeddings = np.load(r'..\SynonymExtraction\Barrons_Words_1000\barron_1000_embeddings.npy')
print("all_embeddings length : ", len(all_embeddings))

def getSynonym(test_str) :
#test_str = 'An exclamation of excitement, surprise, shock'
#test_str = 'The worst kind of person.  You cannot fully construct a meaning that fully encompasses what this vicious insult means.' #  If you are an asshole, you are disgusting, loathesome, vile, distasteful, wrathful, belligerent, agoraphobic, and more.  Assholes are human fecal matter.  They are the lowest of the low.  They transcend all forms of immorality.  It is the very worst of insults; to be called an asshole is to have your very soul ripped apart and shat on.  I say that the word asshole is the worst cussword of the english language, worst than fuck, shit, and cunt combined.'

    X = np.array([test_str])
    text_data = X
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    embeddings = model.encode(text_data, show_progress_bar=False)
    embed_data = embeddings
    X = np.array(embed_data)

    #print("X length : ", len(X[0]))

    best_score = 0
    best_index = 0
    index = 0
    scores = {}
    for barrons in all_embeddings:
        score = get_cosine_similarity(X, barrons)
        scores[score] = index
        if best_score < score :
            best_score = score
            best_index = index
        index += 1

    # creating a data frame
    df = pd.read_csv(r"..\SynonymExtraction\Barrons_Words_1000\barrons_def_1000.csv")
    # print(best_index)
    #print(df['Word'][best_index], " : ", df['Defination'][best_index])

    # sorted_score = collections.OrderedDict(sorted(scores.items(), reverse=True))
    #
    # count = 0
    # for k, index in sorted_score.items():
    #     count += 1
    #     if 5 == count:
    #         break
    #     print("-------------Recommendation---------- :: ", count)
    #     print(df['Word'][index], " : ", df['Defination'][index])

    return df['Word'][best_index]

