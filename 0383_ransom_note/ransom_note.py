class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}  # chars used in magazine.
        
        for c in magazine:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        for c in ransomNote:
            if c in chars:
                if chars[c] < 1:
                    return False
                else:
                    chars[c] -= 1
            else:
                return False
        
        return True
