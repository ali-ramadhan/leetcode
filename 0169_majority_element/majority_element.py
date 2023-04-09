# Hashmap solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        freq = {}  # Keep track of element frequencies
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] > threshold:
                return i

# Boyer–Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = None
        
        for num in nums:
            if counter == 0:
                candidate = num
            counter += (1 if num == candidate else -1)
        
        return candidate
