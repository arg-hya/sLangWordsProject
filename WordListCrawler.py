import string
from bs4 import BeautifulSoup
import urllib.request
import time
import os
import argparse
import re

from FilterPipeline import passFilterPipelineAndGetDefinition, VERBOSE
from NERFilter import applyStanfordNER, applyStanfordNERonExample
from UrbanDictApiInterface import getWord

API = "https://www.urbandictionary.com/browse.php?character={0}"

MAX_ATTEMPTS = 40
DELAY = 10

NUMBER_SIGN = "*"

#count_word = 0


# https://stackoverflow.com/a/554580/306149
class NoRedirection(urllib.request.HTTPErrorProcessor):
    def http_response(self, request, response):
        return response

    https_response = http_response


def extract_page_entries(letter, html):
    soup = BeautifulSoup(html, "html.parser")
    classes = []
    contents = soup.find_all('a', class_='py-1')
    for li in contents:
        word = li.get_text()
        #print("extract_page_entries : ", word)
        sLangWord = word #passThroughFilterPipeline(word)
        if sLangWord :
            #print("Keeping this word: ", sLangWord)
            yield (sLangWord)

def get_next(letter, html):
    soup = BeautifulSoup(html, "html.parser")
    next = soup.find('a', {"rel": "next"})
    if next:
        href = next['href']
        return 'https://www.urbandictionary.com' + href
    return None


def extract_letter_entries(letter):
    url = API.format(letter)
    attempt = 0
    while url:
        print(url)
        response = urllib.request.urlopen(url)
        code = response.getcode()
        if code == 200:
            content = response.read()
            yield list(extract_page_entries(letter, content))
            url = get_next(letter, content)
            attempt = 0
        elif code == 302:
            print("Got all the Words for alphabet ", letter)
            break
        else:
            print(url)
            print(f"Trying again, expected response code: 200, got {code}")
            attempt += 1
            if attempt > MAX_ATTEMPTS:
                break
            time.sleep(DELAY * attempt)


opener = urllib.request.build_opener(NoRedirection, urllib.request.HTTPCookieProcessor())
urllib.request.install_opener(opener)

letters = list(string.ascii_uppercase) + ['#']


def download_letter_entries(letter, file):
    file = file.format(letter)
    print("Output File : ", args.out)
    f = open(file, "w")
    pageNum = 1
    #global count_word
    for entry_set in extract_letter_entries(letter):
        for word in entry_set:
            #count_word = count_word + 1
            sLangWord, definition = passFilterPipelineAndGetDefinition(word)
            if sLangWord :
                print("Keeping this word : ", sLangWord)
                f.write(sLangWord + ' , ' + definition + '\n')
        # if pageNum == 300:
        #     break
        #print("Word number : ", count_word)
        pageNum += 1
    f.close()


def download_entries(letters, file):
    for letter in letters:
        print(f"======={letter}=======")
        download_letter_entries(letter, file)


def fromParticularPageTest():
    print("Starting...")
    url = "https://www.urbandictionary.com/browse.php?character=A&page=1011"
    letter = 'A'
    print("URL : ", url)
    while url:
        print(url)
        response = urllib.request.urlopen(url)
        code = response.getcode()
        if code == 200:
            content = response.read()
            yield list(extract_page_entries(letter, content))
            url = get_next(letter, content)
            attempt = 0
        elif code == 302:
            print("Got all the Words for alphabet ", letter)
            break
        else:
            print(url)
            print(f"Trying again, expected response code: 200, got {code}")
            attempt += 1
            if attempt > MAX_ATTEMPTS:
                break
            time.sleep(DELAY * attempt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Running Crawler...")
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--ifile', dest='ifile',
                        help='input file name. Contains a list of letters separated by a newline', default="input.list")

    parser.add_argument('--out', dest='out',
                        help='output file name. May be a format string', default="data/{0}.csv")

    args = parser.parse_args()

    letters = []
    with open(args.ifile, 'r') as ifile:
        for row in ifile:
            letters.append(row.strip())

    download_entries(letters, args.out)
