from collections import Counter, deque
'''
Need to have a max-heap of (freq, letter) for each non-zero frequency of letter.
This is similar to task scheduler, except now each label/letter has a fixed cooldown of 2.
Have a pq of elements available to be added to result, and a queue for those in cooldown,
when cooldown completed, add it back to pq (max-heap)
'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        c = Counter(s)
        mc = c.most_common(1)[0] #most_common(x) -> list[tuple[str,int]]
        freq = mc[1]
        if freq > (n-freq+1):
            return "" #outnumbers all other elements
        
        hp = [[freq,ltr] for ltr,freq in c.items()]
        heapq.heapify_max(hp)
        q = deque() #stores elements in cooldown - [freq,letter,freeUpTime]

        ans = []
        for t in range(n):
            if q and q[0][2] <= t:
                #free to be re-used now
                freq, ltr, _ = q.popleft()
                if freq > 0: heapq.heappush_max(hp, [freq,ltr])

            if not hp: return "" #no available elements to add
            freq, ltr = heapq.heappop_max(hp)
            ans.append(ltr)
            q.append([freq-1,ltr,t+2]) #add to cooldown
        
        return "".join(ans)