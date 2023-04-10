# Bottom-up dynamic programming approach
def min_ways(coins, amount, memory={}):
    if amount == 0:
        return 0

    if amount < 1:
        return 0
    
    if amount in memory:
        return memory[amount]
    
    if amount in coins:
        memory[amount] = 1
        return memory[amount]
    
    min_ways_minus_a_coin = [min_ways(coins, amount - c, memory) for c in coins]

    # No way to make change.
    if max(min_ways_minus_a_coin) < 1:
        memory[amount] = -1
        return -1
    
    memory[amount] = 1 + min(m for m in min_ways_minus_a_coin if m > 0)
    
    return memory[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return min_ways(coins, amount, {})
