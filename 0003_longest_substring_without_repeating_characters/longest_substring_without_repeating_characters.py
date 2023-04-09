from collections import Counter

# Sliding window [w1, w2) algorithm.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        n = len(s)
        w1 = w2 = 0
        longest = 0

        while w2 < n:
            # Count right-most char.
            r = s[w2]
            chars[r] += 1

            # If we now have more than one of r, shrink the sliding window from the left until we have only 1 of r.
            while chars[r] > 1:
                l = s[w1]
                chars[l] -= 1
                w1 += 1

            longest = max(longest, w2 - w1 + 1)

            # Expand sliding window to the right.
            w2 += 1

        return longest
