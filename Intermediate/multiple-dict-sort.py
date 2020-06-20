from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Harry', 'lname': 'Potter'},
    {'fname': 'James', 'lname': 'Bond'},
    {'fname': 'Mufasa', 'lname': 'Lion'},
    {'fname': 'Uzumaki', 'lname': 'Naruto'},
    {'fname': 'Nobert', 'lname': 'Momoh'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('--------')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)