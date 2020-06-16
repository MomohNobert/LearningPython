def main():
    buffersize = 50000

    infile = open('bigfile.txt', 'r')
    outfile = open('bignew.txt', 'w')

    buffer = infile.read(buffersize)

    while len(buffer):
        outfile.write(buffer)
        print('.', end = ' ')
        buffer = infile.read(buffersize)
    print()
    print('Done.')

if __name__ == "__main__": main()