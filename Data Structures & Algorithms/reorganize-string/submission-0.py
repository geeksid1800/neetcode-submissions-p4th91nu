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
        cnt = Counter(s)
        mc = cnt.most_common(1) #returns a list of n tuples
        char, freq = mc[0] #(char, count)
        if freq > (n-freq+1): 
            #if the most frequent character outnumbers all other chars by more than 1
            return ""
        
        pq = [[-freq,char] for char,freq in cnt.items() if freq>0]
        heapq.heapify(pq)
        time = 0
        q = deque() #(-freq, char, freeup time)
        ans = []

        while pq or q:
            time += 1
            while q and q[0][2] <= time:
                nFreq, char, _ = q.popleft()
                heapq.heappush(pq, [nFreq, char])
            
            if not pq:
                return "" #if all chars are in cooldown, means we don't have a valid char we can add 

            nFreq, char = heapq.heappop(pq)
            ans.append(char)
            if nFreq+1 < 0:
                q.append([nFreq+1,char, time+2])
        
        return "".join(ans)