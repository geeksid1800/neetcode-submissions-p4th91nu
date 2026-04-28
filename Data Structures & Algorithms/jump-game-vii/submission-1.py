from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1': return False
        unique = set([0])

        q = deque([0])
        while q:
            ix = q.popleft()
            if ix==n-1: return True

            for j in range(minJump,maxJump+1):
                if ix+j >= n: break
                if s[ix+j] == '0' and (ix+j) not in unique:
                    q.append(ix+j)
                    unique.add(ix+j)
        
        return False