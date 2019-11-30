from typing import List, Dict, Optional
from collections import defaultdict
import json
import math

FILE_NUM = 7
DOC_TOTAL = 55393


def main():
    global FILE_NUM
    line: List[Optional[str]] = [None] * FILE_NUM
    token_dict: List[Optional[Dict]] = [None] * FILE_NUM

    # Open all the partial indexes and put them in a file descriptor list
    fp = [open("inverted_index_{}.txt".format(x), 'r') for x in range(FILE_NUM)]

    # Load all the tokens in the file's line as a dictionary in token_dict
    index = 0
    while index < FILE_NUM:
        line[index] = fp[index].readline()
        token_dict[index] = json.loads(line[index])
        index += 1

    loop = True
    # valid_i will be currently open files
    valid_i = [x for x in range(FILE_NUM)]

    while loop:

        # Find lowest token alphabetically from currently open lines
        token = min(list(token_dict[x].keys())[0] for x in valid_i)

        # Will put all occurances of that token from partial indexes into one new dictionary
        new_dict = defaultdict(list)

        for index in valid_i:
            if list(token_dict[int(index)].keys())[0] == token:
                for element in token_dict[index][token]:
                    new_dict[token].append(element)
                line[index] = fp[index].readline()
                if not line[index]:
                    valid_i.remove(index)
                    fp[index].close()
                else:
                    try:
                        token_dict[index] = json.loads(line[index])
                    except:
                        pass
                # print("same for {}".format(index))

        # Score the tf-idf s of those postings
        new_dict = scorer(new_dict)
        # And write as 1 line to full index file on disk
        full_index_write(new_dict)
        print(token)

        if not valid_i:
            loop = False


def scorer(token_dict):
    for token in token_dict:
        df = len(token_dict[token])
        idf = math.log(DOC_TOTAL / df)
        for posting in token_dict[token]:
            # tf = posting[1]
            tf_idf = (1 + math.log(posting[1])) * idf
            posting[1] = tf_idf

        # To save some time and space, only return highest 20 tf_idf postings
        token_dict[token].sort(key=lambda x: x[1], reverse=True)
        # token_dict[token] = token_dict[token][0:20]

    return token_dict


def full_index_write(uniques):
    with open("full_index.txt", 'a') as our_index:
        json.dump(uniques, our_index)
        our_index.write("\n")


if __name__ == '__main__':
    main()
