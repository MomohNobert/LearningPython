def main():
    testfunc(1,2,3,4,5,6)

def testfunc(this, that, other, *args):
    print(this, that, other, args)
    for n in args: print(n, end='')

if __name__ == "__main__": main()