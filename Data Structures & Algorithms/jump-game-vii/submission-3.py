from collections import deque
'''
BFS-based solution. From current level (elements in the queue), check which
elements are reachable (this determines the next level). If the q empties before
you find n-1, you don't have a path to it.
Multiple values of (ix,j) can lead to the same ix+j, where ix is current element 
and j is jump dist. We then store a value farthest, noting the farthest ix we can
reach from current level. We update this so future jumps will only cross it. 
'''
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1': return False
        farthest = 0

        q = deque([0])
        while q:
            ix = q.popleft()
            if ix==n-1: return True
            start = max(farthest+1,ix+minJump)
            end = min(n,ix+maxJump+1)
            for nxt in range(start,end):
                if s[nxt] == '0': q.append(nxt)
            farthest = ix + maxJump
        
        return False