import time


def main():
    with open("full_index.txt", 'r') as fp:
        start = time.time()
        i = 0
        line = fp.readline()
        while line:
            line = fp.readline()
            i += 1

        print("Took: ", time.time() - start)
        print("Tokens: ", i)


if __name__ == '__main__':
    main()