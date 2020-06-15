def main():
    try:
        for line in readfile('lxines.xt'): print(line.strip())
    except IOError as e:
        print('cannot read file: ', e)
    except ValueError as e:
        print('bad filename', e)

    # try:
    #     fh = open('xlines.txt')
    # except IOError as e:
    #     print('could not open file.', e)
    # else:
    #     for line in fh: print(line.strip())

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
    

if __name__ == "__main__": main()