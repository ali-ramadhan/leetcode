def combination_sum(candidates, target, combinations, nums=[]):
    for num in candidates:
        if sum(nums + [num]) == target:
            new_combination = tuple(sorted(nums + [num]))
            combinations.add(new_combination)
            break
        elif sum(nums + [num]) < target:
            combination_sum(candidates, target, combinations, nums + [num])
        elif sum(nums + [num]) > target:
            break

    return combinations

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return combination_sum(sorted(candidates), target, set())
