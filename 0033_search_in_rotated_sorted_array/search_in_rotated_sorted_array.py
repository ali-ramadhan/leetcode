class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 0:
            return -1
        
        if n == 1:
            return 0 if nums[0] == target else -1
        
        # First let's find the pivot index k using binary search.
        # It should be the index k such that nums[k-1] > nums[k].
        l = 0
        r = n - 1
        k = None
        while l <= r:
            m = (l + r) // 2
            print(f"l={l}, m={m}, r={r}")

            m_minus_1 = m-1 if m > 0 else n-1
            if nums[m_minus_1] > nums[m]:
                k = m
                break

            # The right portion is sorted so k must be in the left portion.
            elif nums[m] <= nums[r]:
                r = m - 1
            
            # The left portion is sorted so k must be in the right portion.
            elif nums[l] <= nums [m]:
                l = m + 1
            
        print(f"k={k}")

        # Now we do binary search on nums[(k + i) % n] instead of nums[i].
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            print(f"l={l}, m={m}, r={r}")
            if nums[(k + m) % n] == target:
                return (k + m) % n
            elif nums[(k + m) % n] >= target:
                r = m - 1
            elif nums[(k + l) % n] <= target:
                l = m + 1

        return -1
