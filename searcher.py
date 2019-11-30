from collections import defaultdict
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import json
import time
import math

SPLIT_NUM = 22
DOC_TOTAL = 55393


def main():
    ps = PorterStemmer()
    top_scores = defaultdict(int)
    q_uniques = defaultdict(int)
    cos_scores = defaultdict(list)

    with open("cosine_dlower.txt", 'r') as cos_lowers:
        cos_dlower_str = cos_lowers.read()
        cos_dlower = json.loads(cos_dlower_str)

    with open("page_index.txt", 'r') as pages:
        pages_str = pages.read()
        page_index = json.loads(pages_str)

    fp = [open("split_index/split_index_{}.txt".format(x), 'r') for x in range(SPLIT_NUM)]

    query = input("Enter search keywords: ")
    start = time.time()
    query_tokens = word_tokenize(query)
    for token in query_tokens:
        q_uniques[ps.stem(token)] += 1

    for token in q_uniques:
        token_str = '"' + token + '"'
        token_dict = {}
        split_index = find_split_index(token)
        while True:
            try:
                line = fp[split_index].readline()
            except:
                print("Invalid Input")
                break
            if token_str in line:
                token_dict = json.loads(line)
                break
            if not line:
                break

        try:
            q_tf_idf = (1 + math.log(q_uniques[token])) * math.log(DOC_TOTAL/len(token_dict[token]))
        except:
            continue

        # print("Query tf-idf: ", q_tf_idf)

        try:
            for posting in token_dict[token][0:20]:
                try:
                    cos_scores[posting[0]][0] += q_tf_idf * posting[1]
                    cos_scores[posting[0]][1] += q_tf_idf ** 2
                except:
                    cos_scores[posting[0]].append(q_tf_idf * posting[1])
                    cos_scores[posting[0]].append(q_tf_idf ** 2)
        except:
            pass

    # key = doc_id
    for key in cos_scores:
        top_scores[key] += cos_scores[key][0] / (math.sqrt(cos_scores[key][1]) * math.sqrt(cos_dlower[str(key)]))

    # print(top_scores)
    top_scores_sorted = sorted(top_scores.items(), key=lambda kv: kv[1], reverse=True)

    i = 1
    scores = []
    print("Top results for ", query, ": ")
    for page_id, score in top_scores_sorted:
        if score not in scores and i <= 5:
            print(str(i), ": ", page_index[str(page_id)])
            # print("\t Score: ", score)
            scores.append(score)
            i += 1
    else:
        if not top_scores_sorted:
            print("No results found.")

    print("Took: ", time.time() - start)


def find_split_index(token):
    if token <= 'app_cu_bd':
        return 0
    elif token <= 'bierutow':
        return 1
    elif token <= 'caryotin':
        return 2
    elif token <= 'conic':
        return 3
    elif token <= 'dewater':
        return 4
    elif token <= 'endleaf':
        return 5
    elif token <= 'forkhead_n':
        return 6
    elif token <= 'gregori':
        return 7
    elif token <= 'humanid':
        return 8
    elif token <= 'johnboat':
        return 9
    elif token <= 'leki':
        return 10
    elif token <= 'medfield':
        return 11
    elif token <= 'naveen':
        return 12
    elif token <= 'overexposur':
        return 13
    elif token <= 'polychro':
        return 14
    elif token <= 'reflood':
        return 15
    elif token <= 'schulof':
        return 16
    elif token <= 'spaldeen':
        return 17
    elif token < 'tambourinist':
        return 18
    elif token <= 'twopi':
        return 19
    elif token <= 'waitress':
        return 20
    elif token <= 'zzzzzz':
        return 21
    else:
        return None


if __name__ == '__main__':
    main()
