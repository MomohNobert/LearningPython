def main():
    # fh = open('lines.txt')
    # for index, line in enumerate(fh.readlines()):
    #     print(index, line, end = ' ')

    s = 'this is a string'
    for i, c in enumerate(s):
        print(i, c)
        if c == 's': print('index {} is an s'.format(i))

if __name__ == "__main__": main()