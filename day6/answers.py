import sys
from functools import reduce

with open(sys.argv[1]) as answer_fle:
    group_answers = answer_fle.read().split('\n\n')

total1 = 0
total2 = 0

for group in group_answers:
    all_answers = list(filter(None, group.split("\n")))

    # for part one
    total1 += len(set(''.join(all_answers)))

    # for part two
    intersection = reduce(lambda answer1, answer2: set.intersection(set(answer1), set(answer2)), all_answers)
    total2 += len(intersection)

print(f'Part one: {total1}')
print(f'Part two: {total2}')
