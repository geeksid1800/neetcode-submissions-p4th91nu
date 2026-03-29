from heapq import heapify, heappop, heappush
'''
Order trips list by 'from' so we encounter earliest pickup passengers first.
Maintain a min-heap pq for passengers currently on the bus at any point, ordered by 'to'.
Every time we try to pick up new passengers, we update the pq by removing all passengers that would've
gotten off between the previous pickup and this one. Then we try to onboard the new passengers,
if it's not possible (exceeds total capacity), return false.
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda l: l[1], reverse=True) #reversed so we can pop passengers as we onboard
        pq = [] #(to, from, passengers)
        seatsFree = capacity
        print(f"pickup order {trips[::-1]}")
        while trips:
            newStop = trips.pop() #(passengers, from, to)
            while pq and pq[0][0] <= newStop[1]:
                seatsFree += heappop(pq)[2]
                
            print(f"{seatsFree=}, trying to add {newStop[0]}")
            if seatsFree < newStop[0]:
                return False
            seatsFree -= newStop[0]
            
            heappush(pq, newStop[::-1])
        
        return True