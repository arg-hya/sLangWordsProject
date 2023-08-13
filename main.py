import enchant
from nltk.corpus import words
import nltk
nltk.download('words')

def testEnchant():
    d = enchant.Dict("en_US")

    word = "Hello"
    while word != 'quit':
        # Ask the user for a name.
        word = input("Please enter text, or enter 'quit': ")
        print(d.check(word))

def testNLTK():
    word = "Hello"
    while word != 'quit':
        # Ask the user for a name.
        word = input("Please enter text, or enter 'quit': ")
        print(word in words.words())

testNLTK()