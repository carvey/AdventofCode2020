import sys
from functools import reduce
from itertools import combinations

entries_fle = open(sys.argv[1])
combination_size = int(sys.argv[2])

entries = entries_fle.read().strip().split('\n')
entries_fle.close()

entries = [int(entry) for entry in entries]

combinations = combinations(entries, combination_size)

sums = {}

for combination in combinations:
    total = sum(combination)

    # multiply all integers in the combination
    multiple = reduce(lambda x, y: x * y, combination)

    sums[total] = multiple

print(sums[2020])

