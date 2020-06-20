import heapq

grades = [32, 43, 654, 43, 33, 54, 22, 34]

print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 20},
    {'ticker': 'FB', 'price': 301},
    {'ticker': 'MSFT', 'price': 251},
    {'ticker': 'TUNA', 'price': 501},
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))