# We want to find n and m such that n + m = target.
# Keep track of numbers we've seen so far and their index.
# For each number n, check to see if m is in the dict.
# Using a dict makes this O(n).
def twoSum(self, nums: List[int], target: int) -> List[int]:
    needed = {}
    for i, n in enumerate(nums):
        if (target - n) in needed:
            return [needed[target - n], i]
        else:
            needed[n] = i
