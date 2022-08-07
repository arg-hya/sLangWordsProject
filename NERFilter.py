from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
from enum import Enum

from UrbanDictApiInterface import getExampleText

java_path = "C:/Program Files/Java/jre1.8.0_291/bin/java.exe"
os.environ['JAVAHOME'] = java_path

class NerTags(Enum):
	O = 1
	PERSON = 2
	LOCATION = 3
	ORGANIZATION = 4

st = StanfordNERTagger(r'D:\DarkWebResearch\stanford-ner-4.2.0\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser.gz',
					   r'D:\DarkWebResearch\stanford-ner-4.2.0\stanford-ner-2020-11-17\stanford-ner.jar',
					   encoding='utf-8')

#text = "First up in London Alisha will Putin be Riccardo Tisci, onetime Givenchy darling, favorite of Kardashian-Jenners everywhere, who returns to the catwalk with men’s and women’s wear after a year and a half away, this time to reimagine Burberry after the departure of Christopher Bailey."
text = 'Arghya While in France, cHristine Lagarde discussed Zahira short-term stimulus efforts in a Zahiraa recent interview with the Wall Street Journal.'


def applyStanfordNER(text, displayTags = False):
	tokenized_text = word_tokenize(text)
	classified_text = st.tag(tokenized_text)

	if True == displayTags :
		print(classified_text)

	for tup in classified_text:
		tag = tup[1]
		NERTag = NerTags[tag]

		if NerTags.O == NERTag:
			return True
		else :
			print(classified_text)
			return False

def applyStanfordNERonExample(exampleText, word, displayTags = False):
	print(exampleText)
	tokenized_text = word_tokenize(exampleText)
	classified_text = st.tag(tokenized_text)

	if True == displayTags :
		print(classified_text)

	for tup in classified_text:
		if word.lower() == tup[0].lower() :
			tag = tup[1]
			NERTag = NerTags[tag]
			if NerTags.O != NERTag:
				print(tup)
				return False
			else : #Ner Tag is 'O'
				return True

	print("Word : ", word, " Not found in example.")
	return False









import spacy

# sentence = "First up in London Alisha will Putin be Riccardo Tisci, onetime Givenchy darling, favorite of Kardashian-Jenners everywhere, who returns to the catwalk with men’s and women’s wear after a year and a half away, this time to reimagine Burberry after the departure of Christopher Bailey."
#
# from spacy.lang.en.examples import sentences
#
# nlp = spacy.load("en_core_web_sm")
#
# doc = nlp(sentence)
#
# for ent in doc.ents:
#     print(ent.text,ent.label_)

nlp = spacy.load("en_core_web_sm")

def applySpicyNER(text, displayTags = False):
	doc = nlp(text)

	if True == displayTags :
		for ent in doc.ents:
			print(ent.text, ent.label_)
