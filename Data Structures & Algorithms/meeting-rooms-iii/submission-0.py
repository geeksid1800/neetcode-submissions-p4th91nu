from heapq import heapify, heappop, heappush
'''
Create two min-heaps. One for finding the lowest numbered available meeting room,
second for tracking the free-up times of currently occupied rooms.
1) Before your current meeting starts, try clearing up the rooms in which the
meetings have already ended.
2) If there's a room available at the start time of your current meetings, pop it
from the list of available rooms, and use it, setting it into the occupied rooms
heap with the meeting ending time
3) If there's no rooms available, see the earliest ending meeting, and set the 
end time of your current meeting as that old end time + duration of your mtg.
'''
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [i for i in range(n)]
        ends = [] #(end_time,room_no.)
        heapify(available); heapify(ends)
        meetings.sort()
        counts = [0]*n
        max_use = 0

        for mtg in meetings:
            while ends and ends[0][0] <= mtg[0]:
                end_time,room = heappop(ends)
                heappush(available,room)

            if available:
                room = heappop(available)
                heappush(ends,(mtg[1],room))
            else:
                #wait till a room is available
                dur = mtg[1] - mtg[0]
                end_time,room = heappop(ends)
                heappush(ends,(end_time+dur,room))

            counts[room] += 1
            max_use = max(max_use, counts[room])

        for room,uses in enumerate(counts):
            if uses == max_use: return room