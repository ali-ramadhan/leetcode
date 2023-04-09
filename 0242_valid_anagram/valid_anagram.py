class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sc = {}
        tc = {}

        for c in s:
            if c in sc:
                sc[c] += 1
            else:
                sc[c] = 1

        for c in t:
            if c in tc:
                tc[c] += 1
            else:
                tc[c] = 1
        
        return sc == tc
