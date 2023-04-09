class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # subarray_sum[i] is the max subarray sum for nums[0:i].
        max_sum = [0] * n
        max_sum[0] = nums[0]

        for i in range(1, n):
            if max_sum[i-1] > 0:
                max_sum[i] = max_sum[i-1] + nums[i]
            else:
                max_sum[i] = nums[i]
        
        return max(max_sum)
