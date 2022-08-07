import enchant
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from NERFilter import applyStanfordNER, applySpicyNER


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    d = enchant.Dict("en_US")
    print(d.check("Hello"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #text1 = "First up in London Alisha will Putin be Riccardo Tisci, onetime Givenchy darling, favorite of Kardashian-Jenners everywhere, who returns to the catwalk with men’s and women’s wear after a year and a half away, this time to reimagine Burberry after the departure of Christopher Bailey."
    text = 'While Putin in France Fucker Christine Lagarde discussed Zahira short-term Fucker stimulus Buttfuck efforts in a Zahiraa recent interview with the Wall Street Journal.'
    text3 = 'Those kids are little Putins today.'
    words = text.split(" ")
    #print(words)
    applyStanfordNER(text, True)
    print("Performing word base...")
    for word in words:
        applyStanfordNER(word, True)
    #applyStanfordNER(text1, True)
    #applyStanfordNER(text3, True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
