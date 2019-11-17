import os
import glob
import re
import sys
import json
from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from Posting import Posting
import math

page_index = {}


def main():
    uniques = scorer()
    print(len(uniques))

    with open("page_index.txt", 'w') as pages:
        pages.write(json.dumps(page_index))

    with open("inverted_index.txt", 'w') as our_index:
        our_index.write(json.dumps(uniques))


def scorer():
    uniques, doc_count = indexer()
    print("doc_count: " + str(doc_count))

    for token in uniques:
        df = len(uniques[token])
        idf = math.log(doc_count/df)
        for posting in uniques[token]:
            # tf = posting.tf_idf
            this_tf_idf = (1 + math.log(posting.tf_idf)) * idf
            posting.__init__(posting.doc_id, round(this_tf_idf, 2), posting.fields)

    return uniques


def indexer():

    index = 0
    ps = PorterStemmer()
    uniques = defaultdict(list)

    # argv[1] should be something like DEV/** or DEV/[folder]/**
    for page in glob.iglob(sys.argv[1], recursive=True):

        if os.path.isfile(page):
            # Open the json file and read
            print(page)
            with open(page, 'r') as f:
                page_json = f.read()

                # Take the URL of the page and add it to the page index
                page_url = json.loads(page_json)['url']
                page_index[index] = page_url

                # Take the content from the json
                page_content = json.loads(page_json)['content']
                t_tokens = page_content.strip().split()
                tokens = [t for t in t_tokens if re.match(r'[^\W\d]*$', t)]
                f_tokens = ' '.join(tokens)

                nltk_tokens = word_tokenize(f_tokens)
                # print(nltk_tokens)

                for token in nltk_tokens:
                    token = token.lower()
                    token = ps.stem(token)

                    # If doc id already in a posting under that token add 1 to score
                    for posting in uniques[token]:
                        if index is posting.doc_id:
                            posting.__init__(posting.doc_id, posting.tf_idf + 1, posting.fields)
                            break
                    else:
                        uniques[token].append(Posting(index, 1, []))

                print(page_url)

                index += 1

            # TODO: Remove this thing once done with testing 1 page
            # break

    return uniques, index


# def scorer(token):


if __name__ == '__main__':
    main()
