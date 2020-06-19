first = ['Nobert', 'Tom', 'Martha']
last = ['Momoh', 'Hanks', 'Stewart']

names = zip(first, last)

# [('Nobert', 'Momoh'), ('Tom', 'Hanks'), ('Martha', 'Stewart')]
print(names)

for a, b in names:
    print(a, b)