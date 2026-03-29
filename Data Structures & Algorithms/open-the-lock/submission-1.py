from collections import deque
'''
At any configuration, we have 8 possibilities: go one number up or down, for each of
the 4 digits. This would make a purely DFS-based approach too inefficient, as the 
recursion tree would be too large. Also, we'd have to go through every possible way
of reaching the target before we could give an answer. 
Instead, use BFS with a queue: add all 8 possibilities to the q, and whenever you
reach target for the first time, it's guaranteed to be the shortest path to it.
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        banned = set(deadends)
        visited = set()
        q.append('0000')
        ans = 0
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if curr == target:
                    return ans
                if curr in banned or curr in visited:
                    continue

                visited.add(curr)
                curr = list(curr)
            
                #add and subtract one for each digit in curr to create next states
                for i in range(4):
                    nxt, prev = curr.copy(), curr.copy()
                    nxt[i] = str((int(curr[i]) + 1)%10)
                    q.append("".join(nxt))
                    prev[i] = str((int(curr[i]) - 1 + 10)%10)
                    q.append("".join(prev))

            ans += 1
        
        return -1

