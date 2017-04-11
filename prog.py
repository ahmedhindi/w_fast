from numpy import random, arange
from fuzzywuzzy import process
from collections import defaultdict
# from wiki_scraper import *
import re
import pickle


ahmed = 10


def user():
    "returns user name and artical name"
    user_name = input("USER-NAME :> ")
    artical_name = input("wikipedia artical name :> ")
    sent_num = input("the number of sentences :> ")
    return user_name.strip(), artical_name.strip().replace(" ", '_'), sent_num


def store_scores(scores, user_name):
    '''append the user score to his past scores if user doesn't
    exist it creats it'''
    if user_name in d:
        score_list.append(scores)

#
# def sent_token(text):
#     cleaned_dict = []
#     for i in text:
#         cleaned_dict.append(re.sub(" \d+", " ", i).strip())
#     return cleaned_dict


def read_text(file_name):
    "reads txt file of words and returns a list of words"
    with open('dict/{}.pickle'.format(file_name), 'rb') as f:
        return pickle.load(f)


# def show_text(dict):
#     "randomly select a number words of the input dictionary"
#     selected_words = random.choice(dict, num_words)
#     return selected_words
#

def store_text(artical_name, cleaned_text):
    with open('dict/{}.pickle'.format(artical_name), 'wb') as f:
        pickle.dump(cleaned_text, f)


def print_selected(selected_words):
    "prints the selected words"
    print(selected_words)


# def score_user(user_input, selected_words):
#     # print('score_user')
#     """takes the list of user_input and the list of selected words and compare
#     both words and returns score and a list of the words you got wrong """
#     right = 0
#     words = selected_words[0].split(' ')
#     hard_words = []
#     for i in user_input:
#         if i.strip() in words:
#             right += 1
#         else:
#             hard_words.append(process.extractOne(i, words))
#     score = (right / len(words)
#     return score, hard_words
