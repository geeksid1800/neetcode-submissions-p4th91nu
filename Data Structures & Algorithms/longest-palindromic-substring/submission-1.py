class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None]*n for _ in range(n)]
        res, resLen = "",0

        def recur(i,j): #returns True/False if s[i,j] is a palindrome
            nonlocal res, resLen
            '''once you assign res or resLen inside this function, python starts
            treating them as local vars. To prevent that, we need to explicity
            call it nonlocal so it links them to the objects just outside'''
            if i<0 or j>=n or j<i:
                return True
            if dp[i][j] is not None:
                return dp[i][j]

            dp[i][j] = recur(i+1,j-1) and (s[i]==s[j])
            if dp[i][j] and (j-i+1) > resLen:
                res = s[i:j+1]
                resLen = (j-i+1)
            return dp[i][j]
        
        for i in range(n):
            for j in range(i,n):
                recur(i,j)
        return res