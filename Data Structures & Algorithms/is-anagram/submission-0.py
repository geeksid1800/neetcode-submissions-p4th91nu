from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c1.subtract(t)

        for v in c1.values():
            if v != 0:
                return False
        return True
