class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            ways = [1, 2]
            for i in range(2, n):
                ways.append(ways[i-1] + ways[i-2])
            return ways[n-1]
