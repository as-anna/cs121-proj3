import json
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter


def main():
    ps = PorterStemmer()
    scores = {}

    with open("inverted_index.txt", 'r') as f:
        uniques = json.loads(f.read())

        query = input("Enter search keywords: ")
        query_tokens = word_tokenize(query)

        for token in query_tokens:
            try:
                for posting in uniques[ps.stem(token)]:
                    try:
                        scores[posting[0]] += posting[1]
                    except:
                        scores[posting[0]] = posting[1]
            except:
                continue

    top = Counter(scores).most_common(5)

    with open("page_index.txt", 'r') as f:
        pages = json.loads(f.read())

        print("Top results for " + query + ":")
        index = 1
        for key, result in top:
            print(str(index) + ": " + pages[str(key)])
            index += 1


if __name__ == '__main__':
    main()
