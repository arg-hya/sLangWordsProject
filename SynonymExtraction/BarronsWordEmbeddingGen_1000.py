# import pandas module
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import re

from BarronsWikitionaryInterface import getDefinationfromWikiDictionary

# creating a data frame
df = pd.read_csv("Barrons_Words_1000/barrons_def_1000.csv")
print(df.head())
print(len(df['Defination']))
X = np.array(df['Defination'])
print(len(X))
text_data = X
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(text_data, show_progress_bar=True)

embed_data = embeddings

X = np.array(embed_data)
print(len(X))
print(X.shape)
np.save('Barrons_Words_1000/barron_1000_embeddings.npy', X)

# print("Loading Barron's 1000 word databse embedding...")
# all_embeddings = np.load('Barrons_Words_1000/barron_1000_embeddings.npy')
# print("all_embeddings length : ", len(all_embeddings))
# print(all_embeddings.shape)
# if np.array_equal(X,all_embeddings):
#     print("X == all_embeddings  ")

