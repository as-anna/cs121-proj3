import json
from collections import defaultdict


def main():
    cos_lower = defaultdict(int)
    with open("full_index.txt", 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            token_dict = json.loads(line)

            for key in token_dict:
                for posting in token_dict[key]:
                    cos_lower[posting[0]] += posting[1] ** 2

    with open("cosine_dlower.txt", 'w') as outfile:
        for chunk in json.JSONEncoder().iterencode(cos_lower):
            outfile.write(chunk)


if __name__ == '__main__':
    main()
