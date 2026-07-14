from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        c = Counter(s)
        c.subtract(t)
        for v in c.values():
            if v!= 0: return False
        return True