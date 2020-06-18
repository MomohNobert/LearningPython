class Fish:

    def __init__(self):
        print('Glip! Glip!')

    def swim(self):
        print('I am swimming.')

tuna = Fish()

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(10)
rosharch = Enemy(15)
jason.get_energy()
rosharch.get_energy()