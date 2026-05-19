from math import gcd
'''
Brute-force solution. Find the gcd of the lengths of both strings, say it's n.
Iterating i from n till 1, take all i-sized prefixes of either string, and see if 
we can fully construct str1 and str2 with it.
If so, immediately return the substring, otherwise move to a smaller i.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2: return ""
        n1,n2 = len(str1), len(str2)

        n = gcd(n1,n2)
        for i in range(n,0,-1):
            t = str2[:i]
            if (t*(n1//i) == str1) and (t*(n2//i) == str2): return t
        return "" 