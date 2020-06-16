numbersTaken = [2, 5, 12, 13, 17]

print("Here are the available numbers.")

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)