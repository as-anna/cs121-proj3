import sys

FILE_NUM = 7


def main():
    global FILE_NUM
    line = [None] * FILE_NUM

    # Open all the partial indexes and put them in a file descriptor list
    fp = [open("inverted_index_{}.txt".format(x), 'r') for x in range(FILE_NUM)]

    index = 0
    while index < FILE_NUM:
        line[index] = fp[index].readline()


if __name__ == '__main__':
    main()
