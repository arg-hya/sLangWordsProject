# import pandas module
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import collections

from sklearn.metrics.pairwise import cosine_similarity


def get_cosine_similarity(feature_vec_1, feature_vec_2):
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]

all_embeddings = np.load('barron_333_embeddings.npy')

print(len(all_embeddings[0]))

#test_str = 'An exclamation of excitement, surprise, shock'
test_str = 'a person who sucks up to people in a position of authority in order to get some kind of reward or perks'

X = np.array([test_str])
text_data = X
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(text_data, show_progress_bar=True)

embed_data = embeddings

X = np.array(embed_data)

print(len(X[0]))

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
df = pd.read_csv("barron_333.csv")
print(best_index)
print(df['word'][best_index])
print(df['definition'][best_index])

sorted_score = collections.OrderedDict(sorted(scores.items(), reverse=True))

count = 0
for k, index in sorted_score.items():
    count += 1
    if 5 == count:
        break
    print("-------------Recommendation---------- :: ", count)
    print(df['word'][index])
    print(df['definition'][index])


