class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # If we have fewer than three numbers, then no triplets exist.
        if n < 3:
            return []
        
        nums.sort()
        
        # If the array consists of all +ve numbers, then no triplet can sum to zero.
        if nums[0] > 0:
            return []

        # We want to be able to look up numbers and their indices/loc(ation) in O(1) time.
        loc = {}
        for i, num in enumerate(nums):
            loc[num] = i
        
        triplets = set()

        # For all (i, j) pairs, check to see if we can form a triplet nums[i] + nums[k] + nums[k] == 0.
        # Here i < j since nums is sorted.
        for i in range(n-2):
            for j in range(i+1, n-1):
                target = -(nums[i] + nums[j])
                if target in loc:
                    if loc[target] != i and loc[target] != j:
                        k = loc[target]
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        triplets.add(triplet)
        
        return triplets
