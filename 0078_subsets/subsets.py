class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        lz = n # Number of leading zeros needed in binary representation of 2**n.

        power_set = []
        for i in range(2**n):
            b = [int(d) for d in f"{i:0{lz}b}"]
            s = []
            for j, d in enumerate(b):
                if d == 1:
                    s.append(nums[j])
            power_set.append(s)
        
        return power_set
