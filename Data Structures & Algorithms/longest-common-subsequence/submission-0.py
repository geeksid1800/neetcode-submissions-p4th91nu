'''
Consider respective indices i1 and i2 for text1 and text2.
1) If chars at i1 and i2 are the same, proceed with both ix one step forward.
2) If there's a mismatch, you have two decisions for which ix to increment.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[None]*n2 for _ in range(n1)]

        '''Returns: the length of the longest common substrings between
        text1[i1:] and text2[i2:]'''
        def LCS(i1, i2):
            if i1>=n1 or i2>=n2: return 0
            if dp[i1][i2] is not None: return dp[i1][i2]

            if text1[i1] == text2[i2]: dp[i1][i2] = 1 + LCS(i1+1,i2+1)
            else: dp[i1][i2] = max(LCS(i1+1,i2), LCS(i1,i2+1))
            
            return dp[i1][i2]

        return LCS(0,0)