from typing import List, Dict, Optional
from collections import defaultdict
import json

FILE_NUM = 7


def main():
    global FILE_NUM
    line: List[Optional[str]] = [None] * FILE_NUM
    token_dict: List[Optional[Dict]] = [None] * FILE_NUM

    # Open all the partial indexes and put them in a file descriptor list
    fp = [open("inverted_index_{}.txt".format(x), 'r') for x in range(FILE_NUM)]

    index = 0
    while index < FILE_NUM:
        line[index] = fp[index].readline()
        token_dict[index] = json.loads(line[index])
        index += 1

    loop = True
    valid_i = [x for x in range(FILE_NUM)]
    print(valid_i)
    while loop:

        token = min(list(token_dict[x].keys())[0] for x in range(FILE_NUM))
        print(token)

        new_dict = defaultdict(list)

        for index in valid_i:
            print(token_dict[index])
            print(list(token_dict[int(index)].keys())[0])
            if list(token_dict[int(index)].keys())[0] == token:
                new_dict[token].append(token_dict[index][token])
                print("same for {}".format(index))

        print(new_dict)
        loop = False


if __name__ == '__main__':
    main()
