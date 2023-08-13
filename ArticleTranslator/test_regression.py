# Press the green button in the gutter to run the script.
from ArticleParser.ArticleParseReplace import ParserReplacer
from ArticleTranslator.Translator import Translator

if __name__ == '__main__':
    replace = True
    parserReplacer = ParserReplacer(replacer = True)
    inputFilePath = "../ArticleParser/DemoInput.txt"
    with open(inputFilePath, 'r') as file:
        input_data = file.read()
    print("Parsing = True and Replacing = ", replace)

    output_replacer = parserReplacer.parseAndReplace(input_data)
    with open("../ArticleParser/DemoOutput.txt", "a+") as text_file:
        text_file.write(output_replacer)
    print(output_replacer)

    print("Translating text ...")
    translator = Translator(verbose=False)
    para_phrases = translator.translate(output_replacer, input_data)
    print("Translated text :")
    print(para_phrases)
    with open("../ArticleParser/DemoOutput_para.txt", "a+") as text_file:
        text_file.write(para_phrases)