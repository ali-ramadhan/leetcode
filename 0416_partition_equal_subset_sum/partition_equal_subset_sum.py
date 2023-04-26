# Can a subset of nums sum to S?
def subset_sum(nums, S, i, memory):
    key = (S, i)
    if key in memory:
        return memory[key]
    
    if S == 0:
        memory[key] = True
        return True
    
    if S < 0 or i >= len(nums):
        memory[key] = False
        return False

    result = subset_sum(nums, S-nums[i], i+1, memory) or subset_sum(nums, S, i+1, memory)
    memory[key] = result
    return result

def can_partition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, then no partition exists.
    if total_sum % 2 == 1:
        return False

    # Can a subset of nums sum to total_sum/2?
    # If so, then the complement subset must also sum to total_sum/2 and we know a partition exists.
    return subset_sum(nums, total_sum // 2, 0, {})

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return can_partition(nums)
