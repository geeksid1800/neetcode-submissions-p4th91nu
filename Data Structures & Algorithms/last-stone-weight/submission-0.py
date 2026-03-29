from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-1*x for x in stones] #implementing MAX-HEAP
        heapify(pq)
        while len(pq) > 1:
            s1, s2 = heappop(pq), heappop(pq)
            diff = abs(s1-s2)
            if diff>0:
                heappush(pq, -1*diff)
        
        if len(pq):
            return -1*pq[0]
        return 0