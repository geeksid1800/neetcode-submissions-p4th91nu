from collections import deque
'''
Similar to #767.Reorganize String and #621.Task Scheduler.
Except, instead of no consecutive repetitions, we can allow 2 consecutive elements.
So when we choose to add an element to the answer, if the previous element in ans is also the same
char, we put it in cooldown, or else if it's just the first time, we re-add it back to same pq.
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        pq = [it for it in [(-a,'a'), (-b,'b'), (-c,'c')] if it[0]]
        heapq.heapify(pq)
        q = deque() #(nCnt, char, freeUpTime)
        t = 0
        while pq or q:
            t += 1
            while q and q[0][2] <= t:
                nCnt, char, f = q.popleft()
                heapq.heappush(pq, (nCnt, char))
            
            if not pq:
                #no valid elements that we can add at this point, end the solution
                return "".join(ans)

            nCnt, char = heapq.heappop(pq)
            nCnt += 1
            #if it's been same two elements in a row, put it in cooldown, otherwise we can reuse
            if nCnt:
                if ans and ans[-1] == char:
                    q.append((nCnt, char, t+2))
                else:
                    heapq.heappush(pq, (nCnt, char))

            ans.append(char)
            
        return "".join(ans)