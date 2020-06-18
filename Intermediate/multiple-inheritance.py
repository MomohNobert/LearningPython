class Mario():
    def move(self):
        print('I like to move it, move it!')

class Shroom():
    def eat_shroom(self):
        print('Bigger me!')

class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()