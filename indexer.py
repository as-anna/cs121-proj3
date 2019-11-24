import os
import glob
import re
import sys
import json
from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import math
from bs4 import BeautifulSoup

important_word_weight = 2
page_index = {}
ps = PorterStemmer()


def main():
    uniques = scorer()

    sorted_uniques = sorted(uniques.items())

    with open("page_index.txt", 'w') as pages:
        for chunk in json.JSONEncoder().iterencode(page_index):
            pages.write(chunk)

    write_inverted_to_file(sorted_uniques)


def write_inverted_to_file(sorted_uniques):
    with open("inverted_index.txt", 'w') as our_index:
        for chunk in json.JSONEncoder().iterencode(sorted_uniques):
            our_index.write(chunk)


def scorer():
    uniques, doc_count = indexer()
    print(len(uniques))
    print("doc_count: " + str(doc_count))

    for token in uniques:
        df = len(uniques[token])
        idf = math.log(doc_count/df)
        for posting in uniques[token]:
            this_tf_idf = (1 + math.log(posting[1])) * idf
            posting[1] = round(this_tf_idf, 2)

    return uniques


def indexer():

    index = 0
    uniques = defaultdict(list)

    # argv[1] should be something like DEV/** or DEV/[folder]/**
    for page in glob.iglob(sys.argv[1], recursive=True):

        if os.path.isfile(page):
            # Open the json file and read
            try:
                # Take the URL of the page and add it to the page index
                page_url = json.load(open(page))['url']
                page_index[index] = page_url

                # Take the content from the json
                page_content = json.load(open(page))['content']
                t_tokens = page_content.strip()

                soup = BeautifulSoup(page_content, "html.parser")
                important = []
                try:
                    for word in soup.title.string.split():
                        word = word.lower()
                        if ps.stem(word) not in important and ps.stem(word).isalnum():
                            important.append(ps.stem(word))
                except:
                    pass

                for tag_texts in soup.find_all(["h1", "h2", "h3", "b"]):
                    try:
                        # print(tag_texts.string.split())
                        taken_text = tag_texts.string.split()
                        for text in taken_text:
                            text = text.lower()
                            if ps.stem(text) not in important and text.isalnum():
                                important.append(ps.stem(text))
                    except:
                        pass

                # print(important)

                t_tokens = t_tokens.split()

                tokens = [t for t in t_tokens if re.match(r'[^\W\d]*$', t)]
                f_tokens = ' '.join(tokens)

                nltk_tokens = word_tokenize(f_tokens)

                for token in nltk_tokens:

                    token = token.lower()
                    token = ps.stem(token)

                    # If doc id already in a posting under that token add 1 to score
                    for posting in uniques[token]:
                        if index is posting[0]:
                            posting[1] += 1
                            if token in important:
                                posting[1] += important_word_weight
                                # posting[2] += 1
                            break
                    else:
                        uniques[token].append([index, 1])
                        # uniques[token].append([index, 1, 0])

                print(page_url)

                index += 1
                print(index)
            # TODO: Remove this thing once done with testing 1 page
            # break

            except KeyboardInterrupt:

                with open("page_index.txt", 'w') as pages:
                    for chunk in json.JSONEncoder().iterencode(page_index):
                        pages.write(chunk)

                with open("inverted_index.txt", 'w') as our_index:
                    for chunk in json.JSONEncoder().iterencode(uniques):
                        our_index.write(chunk)

                quit()

    return uniques, index


if __name__ == '__main__':
    main()
