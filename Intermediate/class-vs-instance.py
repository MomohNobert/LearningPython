class Girl:
    gender = 'female'
    # class variabes = variables by default

    def __init__(self, name):
        self.name = name
        # unique to each object, an instance variable.

r = Girl('Rachel')
s = Girl('Sophie')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)