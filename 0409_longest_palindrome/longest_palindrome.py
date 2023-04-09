class Solution:
    # We can construct a palindrome using two copies of any letter.
    # If we have an even number N of a letter, we use all N.
    # If we have an odd number M of a letter, we use M-1 of them.
    # If we have any leftover letters with odd frequency, we can put it in the middle for an extra length of 1.
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        
        count = 0
        any_odd = False
        for c in chars:
            if chars[c] % 2 == 0:
                count += chars[c]
            else:
                count += chars[c] - 1
                if not any_odd:
                    count += 1
                    any_odd = True
        
        return count
