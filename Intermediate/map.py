income = [10, 20, 30, 40]

def addTen(dollars):
    return dollars + 10

addedIncome = list(map(addTen, income))
print(addedIncome)