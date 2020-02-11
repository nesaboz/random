# daily problem # 1
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

elements = [10, 2, 15, 3, 7, 10, 7]

k = 17
result = []
hash = {}
tracker = {}  # adds a key: True where key is the number that passes

for x in elements:
    try:
        if tracker[x]:
            continue
    except KeyError:
        tracker[x] = True

    hash[k - x] = x  # we are populating the hash function, so hash[7] = 10

    try:
        result.append((x, hash[x]))  # this means we have a pair, 7 and hash[7]
    except KeyError:
        pass # this just means we don't have a pair
print(result)
