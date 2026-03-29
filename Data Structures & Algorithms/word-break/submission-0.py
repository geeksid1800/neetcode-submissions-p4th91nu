class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [None]*(n+1)

        def recur(s):
            '''given a string s, try to find a 'i' such that s[0,i] is a valid word
            and the rest s[i+1:] can also be broken into valid word(s)'''
            if len(s) == 0: return True
            if dp[len(s)] is not None:
                return dp[len(s)]

            for i in range(len(s)):
                if s[:(i+1)] in wordSet and recur(s[i+1:]):
                    dp[len(s)] = True
                    return True
            dp[len(s)] = False
            return False
        
        return recur(s)