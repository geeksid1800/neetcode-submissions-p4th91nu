'''
Similar to #1094. Car Pooling
Sort by lowest cost/capital reqd projects.
Maintain a pq of projects you can currently afford, sorted by highest profit (to select greedily).
Whenever you complete a project and your budget increases, add all projects you can now afford to
the pq (max-heap).
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [x for x in zip(capital, profits)]
        projects.sort(reverse=True) #(capital, profit) sorted by capital reqd in desc. order

        pq = [] #max-heap highlighting the most profitable projects we can currently take up
        while k:
            while projects and projects[-1][0] <= w:
                cap, profit = projects.pop() #this is now a viable project, add to available projects
                heapq.heappush(pq, -profit)

            if not pq:
                #there are no viable projects we can take up with current capital
                return w
            
            profit = -heapq.heappop(pq)
            w += profit
            k -= 1
        
        return w