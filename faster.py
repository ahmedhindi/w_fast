from prog import *
from wiki_scraper import *
from nltk.tokenize import sent_tokenize, word_tokenize


def main():

    user_name, artical_name, sent_num = user()
    is_stored = check_wiki_art(artical_name)

    if is_stored:
        # read from disk
        print('yaaaaaaay0')
        data = read_text(artical_name)

    else:
        # scrape
        scraped = scrape_art(artical_name)
        print('yaaaaay1', scraped[:1])
        # cleaned data
        data = cleaner(scraped)

        print('yaaaaaaaaay2', data[0])
        # make corpus
        corp = make_corp(data)
        tokens = tokenize(corp)
        # store
        store_text(artical_name, tokens)


def sents(list_of_data, sent_num):
    alist = []
    for i in list_of_data:
        alist.append

        # print sent by sent and score
    for i in sent_num:

    for i in data:
        # print_selected()
        # user_in=user_input()
        # score=score_user(user_in, selected_words)[0]
        # print(score)
        # store_scores(scores=score)
        print(i)
        break


if __name__ == "__main__":
    main()
