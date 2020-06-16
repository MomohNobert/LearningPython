import continue_module

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(1,2,3)
continue_module.printNumbers()