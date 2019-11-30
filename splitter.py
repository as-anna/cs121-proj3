SPLIT_INDEX = 0


def main():
    global SPLIT_INDEX
    token_index = 0

    with open('full_index.txt', 'r') as full_fp:

        while True:

            with open('split_index/split_index_%s.txt' % SPLIT_INDEX, 'a') as split_fp:
                line = full_fp.readline()
                if not line:
                    break
                split_fp.write(line)

                if token_index % 10000 == 0 and token_index != 0:
                    SPLIT_INDEX += 1

                token_index += 1


if __name__ == '__main__':
    main()
