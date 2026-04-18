'''
since s3 is supposed to be made from interweaving s1,s2, it supposed to have
the same characters as s1,s2. Define the recursive function recur(i1,i2) as
returning if you can make s3[i1+i2:] from s1[i1:] and s2[i2:]
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if len(s3) != n1+n2: return False
        dp = [[None]*(n2+1) for _ in range(n1+1)]

        def recur(i1, i2) -> bool:
            i = i1+i2
            if i == n1+n2: return True #found all chars in s3
            if dp[i1][i2] is not None: return dp[i1][i2]
            
            if i1 < n1 and (s1[i1]==s3[i]) and recur(i1+1,i2):
                dp[i1][i2] = True
                return True
            if i2 < n2 and (s2[i2]==s3[i]) and recur(i1,i2+1):
                dp[i1][i2] = True
                return True

            dp[i1][i2] = False
            return False
        
        return recur(0,0)