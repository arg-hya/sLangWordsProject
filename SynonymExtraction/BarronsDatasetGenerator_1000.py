# import pandas module
import pandas as pd
import numpy as np
import re

from BarronsWikitionaryInterface import getDefinationfromWikiDictionary

# creating a data frame
df = pd.read_csv("Barrons_Words_1000/words.csv",  header=0)
df["Defination"] = "NAN"

print(df.keys())
print(df.head())
# iterate through each row and select
for index, row in df.iterrows():
    print("Word : ", row['Word'])
    defination = getDefinationfromWikiDictionary(row['Word'])
    #print(defination)
    if defination:
        defination = defination.strip()
        defination = re.sub('[;,!@#$]', '', defination)
        #df[row['Defination']] = defination
        df['Defination'][index] = defination

#print(df)
df.to_csv("Barrons_Words_1000/barrons_def_1000.csv", sep=',', encoding='utf-8', index=False)