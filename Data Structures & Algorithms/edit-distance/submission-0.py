class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1,n2 = len(word1),len(word2)
        dp = [[None]*n2 for _ in range(n1)]

        #Returns: edit distance between word1[i1:] and word2[i2:]
        def recur(i1,i2):
            if i1==n1: return n2-i2
            if i2==n2: return n1-i1
            if dp[i1][i2] is not None: return dp[i1][i2]

            if word1[i1]==word2[i2]:
                dp[i1][i2] = recur(i1+1,i2+1)
            else:
                #we got 3 choices. Insert word2[i2], delete word1[i1] or sub them
                dp[i1][i2] = 1 + min(
                    recur(i1,i2+1), #inserted word2[i2] before word1[i1]
                    recur(i1+1,i2), #removed word1[i1] from word1
                    recur(i1+1,i2+1) #subbed word1[i1] with word2[i2]
                )
            return dp[i1][i2]
        
        return recur(0,0)