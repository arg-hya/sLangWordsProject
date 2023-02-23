# import pandas module
import pandas as pd
import numpy as np
import re

from BarronsWikitionaryInterface import getDefinationfromWikiDictionary

# creating a data frame
df = pd.read_csv("barrons.csv", names=["word"])
df["Defination"] = "NAN"


# iterate through each row and select
for ind in df.index:
    print("Index : ", ind)
    word = df['word'][ind]
    defination = getDefinationfromWikiDictionary(word)
    if defination:
        defination = defination.strip()
        defination = re.sub('[;,!@#$]', '', defination)
        df.at[ind, 'Defination'] = defination
        #df['Defination'][ind] = defination

#print(df)
df.to_csv("barrons_def.csv", sep=',', encoding='utf-8', index=False)