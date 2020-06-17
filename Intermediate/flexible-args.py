from continue_module import printNumbers

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(1,2,3)
printNumbers()