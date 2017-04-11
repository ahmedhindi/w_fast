import requests
from bs4 import BeautifulSoup
import pickle
import re
import os
# from prog import *

# u = user()[1]


def scrape_art(art_name):
    "returns all text in <p> tags in a wikipedia page"
    rootdir = 'https://en.wikipedia.org/wiki/{}'.format(art_name)
    headers = {'User-Agent': 'Mozilla/5.0'}
    page_html = requests.get(url=rootdir, headers=headers).text
    soup = BeautifulSoup(page_html, 'html.parser')
    alist = []
    for i in soup.find_all('p'):
        alist.append((i.text))
    return alist


def cleaner(list_of_p):
    cleaned = []
    for i in list_of_p:
        cleaned.append(re.sub('\[\d*\]', ' ', i).strip())
    return cleaned


scrape_art(art_name='data')


def make_corp(pt_list=scrape_art):
    "takes a python list of strings returns a text corpus "
    corp = ''
    for i in pt_list:
        corp = corp + '. ' + i
    # pickle the data
    pickle.dump(corp, open("dict/{}.pickle".format(art_name), "wb"))
    return corp


def check_wiki_art(artical_name):
    """
    takes the user input (the artical name) and checks if its in the dicts file
    outputs
     - bool (is the file on the disk of not)
     - a list of all file names for all files in dict dictionary
    """
    list_of_text_files = []

    for i in os.listdir('dict/'):
        list_of_text_files.append(i.split('.')[0])
    # print(list_of_text_files)
    return artical_name.lower() in list(map(str.lower, list_of_text_files))


# print(make_corp())
