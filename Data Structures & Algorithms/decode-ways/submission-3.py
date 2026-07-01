'''Split s into one char or two chars prefix and if those prefixes as valid,
the number of ways of decoding s, is the number of ways the recursive subproblems
can be decoded.
Eg s = 123456, split it as 1,23456 and 12,3456. Since both prefixes are valid,
total ways of decoding s is the sum of ways of decoding 23456 and 3456.
Pure recursion TLEs, we need to implement DP.
dp[i] represents the number of ways to decode s[i:], ie the last n-i chars,
so dp[i] depends on dp[i+1] and dp[i+2]
'''
def isValid(s: str):
    if len(s) == 0: return True
    if s[0] == "0": return False
    n = int(s)
    return n>0 and n<27

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [None]*len(s)
        n = len(s)
        def recur(s):
            if len(s) == 0: return 1
            if s[0] == '0': return 0
            ans = 0
            if dp[n-len(s)] is not None: return dp[n-len(s)]
            if isValid(s[:1]): ans += recur(s[1:])
            if len(s)>1 and isValid(s[:2]): ans += recur(s[2:])
            dp[n-len(s)] = ans
            return ans

        return recur(s)