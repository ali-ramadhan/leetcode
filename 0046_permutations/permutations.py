def remove_number(lst, num):
    return [i for i in lst if i != num]

def _permute(nums, permutations, current_permutation=[]):
    if nums == []:
        permutations.add(tuple(current_permutation))
        return permutations

    for num in nums:
        _permute(remove_number(nums, num), permutations, current_permutation + [num])
    
    return permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return _permute(nums, set())
