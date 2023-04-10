class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        
        prefix = 1  # accumulate prefix product
        suffix = 1  # accumulate suffix product
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]
            ans[-1-i] *= suffix
            suffix *= nums[-1-i]
        
        return ans
