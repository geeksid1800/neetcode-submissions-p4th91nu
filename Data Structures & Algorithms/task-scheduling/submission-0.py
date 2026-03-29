from collections import deque, Counter
from heapq import heapify, heappop, heappush
'''
1) It makes most sense to build a solution around the most frequent label at the moment.
Let's say tasks = [A,A,A,B,B,C,C] n=2
As we can fit other elements in the gaps required by A => A__A__A => ABCABCABC
However, if we build soln around C => C__C => CABCAB_A (have to leave 2 intervals between As)
2) The labels themselves don't matter. Eg. the A could be Z and our total time taken would be same.
All we need is the distinct counts. Eg [A,B,C,A,B,C,A] can be represented as [3,2,2]
3) Construct a max-heap pq to retrieve, at any point, the count of the most frequent label.
Also maintain the current time (i.e. time intervals since start). Pop the most frequent label
from pq, reduce it's freq by 1 (ie. currently processing 1 task of that label), and then add it's
reduced freq and free-up time i.e. the next time when that label can be processed
(current time + n + 1) to a queue that we maintain.
4) When any of the items in the queue are ready to be processed (current time >= free-up time),
pop them from queue and add them back to pq (i.e. their freq goes back into max-heap)
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        counts = [0 for _ in range(26)]
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        counts = [-1*c for c in counts if c>0] #negative due to max-heap

        heapify(counts)
        q = deque() #will store (-freq,free-up time) of labels currently in cooldown
        # print(f"initially {counts=}")

        while counts or q:
            t += 1
            while q and q[0][1] <= t: #add back any labels that have finished cooldown
                front = q.popleft() #front = (-freq, free-up time)
                heappush(counts, front[0])
            
            if counts:
                currFreq = -1*heappop(counts)
                # print(f"reached here, {currFreq=}")
                currFreq -= 1 #choose to process label with highest frequency, 1 instance done
                if currFreq > 0:
                    q.append([-1*currFreq, t+n+1])
            # else:
                # print(f"No labels available to be processed")
            # print(f"{t=}, {counts=}, {q=}")
            
        return t