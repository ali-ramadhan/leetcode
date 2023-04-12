class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        l = 0      # nums[1:l] should be red
        m = 0      # nums[l+1:m] should be white
        r = n - 1  # nums[m+1:r] should be blue
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
        return nums

            
