import time
import sys
import json


def main():
    with open(sys.argv[1], 'r') as fp:
        start = time.time()
        i = 0
        while True:
            line = fp.readline()
            if not line:
                break
            # line_dict = json.loads(line)
            if sys.argv[2] in line:
                print(sys.argv[2])
                print(line)
                line_dict = json.loads(line)
                # break
            i += 1
        print("Took: ", time.time() - start)
        print("Tokens: ", i)


if __name__ == '__main__':
    main()
