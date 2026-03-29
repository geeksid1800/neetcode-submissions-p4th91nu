def isValid(s: str):
    if len(s) == 0: return True
    if s[0] == "0": return False
    n = int(s)
    return n>0 and n<27

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [None]*n
        #dp[i] stores the answer for # of ways to make valid versions of s[i:]

        def recur(s) -> int:
            if len(s) == 0:
                return 1
            if dp[n-len(s)] is not None:
                return dp[n-len(s)]
            ans = 0
            #try to split the string s into valid letter-mapped ints and count.
            #step 1: find the split for the first segment to end, s[0,i]
            for i in range(len(s)):
                if isValid(s[:i+1]):
                    ans += recur(s[i+1:])
            
            dp[n-len(s)] = ans
            return ans

        return recur(s)