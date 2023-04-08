import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = math.inf
        high = 0
        max_profit = 0
        for p in prices:
            if p < low:
                low = p

            potential_profit = p - low
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit
