from ArticleTranslator.Translator import Translator


def testTranslator():
    output_replacer = "Hello"
    while output_replacer != 'quit':
        print("Translating text ...")
        translator = Translator(verbose=True)
        output_replacer = input("Please enter text, or enter 'quit': ")
        #"Keeks is a menace she despises everyone, lol I walked into a conversation like this."
        input_data = "aaaaaa"
        para_phrases = translator.translate(output_replacer, input_data)
        print("Translated text :")
        print(para_phrases)

testTranslator()