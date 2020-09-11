# Find the minimum coin count for changing

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # divisor
    n %= coin # remainder

print(count)