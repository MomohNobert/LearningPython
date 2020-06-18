class Parent():

    def print_last_name(self):
        print('Roberts')

class Child(Parent):

    def print_first_name(self):
        print('Nobert')

    def print_last_name(self):
        print('Momoh')


nobert = Child()
nobert.print_last_name()
nobert.print_first_name()