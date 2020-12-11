import sys
from itertools import combinations

with open(sys.argv[1]) as nums_fle:
    nums = list(map(int, nums_fle.read().split()))

# part 1
special_num = None
step = 25
for i, num in enumerate(nums[25:]):
    sum_nums = map(sum, combinations(nums[i:step], 2))
    step += 1
    if num not in sum_nums:
        special_num = num
        break
    
# part 2
min_max_sum = None
for start in range(0, len(nums)):
    for size in range(0, len(nums)):
        groups = sum(nums[start : start + size])

        if groups == special_num:
            slce = nums[start:start+size]
            min_max_sum = min(slce) + max(slce)
            break


print(f"Part one is: {special_num}")
print(f"Part two is: {min_max_sum}")
