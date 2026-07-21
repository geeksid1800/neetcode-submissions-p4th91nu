from heapq import heappush, heapreplace

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostCommon = [] #min-heap to store most freq elements
        counts = dict()
        for num in nums: counts[num] = counts.get(num,0)+1
        for num,count in counts.items():
            if len(mostCommon)<k:
                heappush(mostCommon, (count,num))
            elif mostCommon[0][0] < count:
                heapreplace(mostCommon, (count,num))
            
        return [tup[1] for tup in mostCommon]