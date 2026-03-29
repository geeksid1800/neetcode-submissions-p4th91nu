from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedBy = defaultdict(int)
        trusts = defaultdict(int)

        for a,b in trust: #a trusts b
            trustedBy[b] += 1
            trusts[a] += 1
        
        for i in range(1,n+1):
            if trustedBy[i] == n-1 and trusts[i] == 0:
                return i
        
        return -1