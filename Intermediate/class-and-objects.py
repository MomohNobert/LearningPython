class Enemy:
    life = 3

    def attack(self):
        print('Ouch!')
        self.life -= 1
        self.checkLife()
        print()

    def checkLife(self):
        if self.life <= 0:
            print('So longgggg!!!!, Cruel World')
        else:
            print(str(self.life) + " lives left")

asmophel = Enemy()

asmophel.attack()
asmophel.attack()
asmophel.attack()