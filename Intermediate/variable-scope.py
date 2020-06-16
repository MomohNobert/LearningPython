a = 123

#if it's created outside or above, it can use it.

def corn():
    # only corn can access in scope
    # a = 123
    print(a)

def fudge():
    print(a)

corn()
fudge()