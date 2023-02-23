# import pandas module
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import re

from BarronsWikitionaryInterface import getDefinationfromWikiDictionary

# creating a data frame
df = pd.read_csv("barron_333.csv")
print(df.head())

X = np.array(df['definition'])
text_data = X
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(text_data, show_progress_bar=True)

embed_data = embeddings

X = np.array(embed_data)

np.save('barron_333_embeddings.npy', X)