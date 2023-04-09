class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        S = set()
        for num in nums:
            if num in S:
                return True
            else:
                S.add(num)
        return False
