from collections import Counter
from heapq import heapify, heappop
'''
The basis of this problem: Both the smallest and largest element in the array
decide the straights that are going to be made. For example, if the smallest ele
in array is 4, and groupSize is 3, then 5 and 6 MUST be there in the array and
also they need to be part of 4's group. So we can remove these 3 elements and
repeat it for the next smallest remaining element in the array at that point.
So we find the smallest element in the array while starting any new group using
a heap (logn time), and use a hashmap to quickly check if the remaining members
are present too, and if so, remove them from the hashmap and heap (if that was
the last occurence of the element)
For a case like [1,2,2,3,4..] and groupSize=3, when we try to reduce the freq of 3
for the first straight, we see that it's not the smallest element in the heap 
(bec. of repeated '2'). This means the next group will have a 2, but no 3, and this
would immediately make our answer False, as there's no valid straight for the 2.
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize != 0: return False
        numGroups = n // groupSize

        freq = Counter(hand)
        hp = [k for k in freq.keys()]
        heapify(hp)

        for _ in range(numGroups): #make groups one by one
            if not hp: return False
            first = hp[0]
            for i in range(groupSize):
                curr = first+i #we need first+0,first+1...first+groupSize-1
                if freq[curr] == 0: return False
                freq[curr] -= 1
                if freq[curr] == 0:
                    if hp[0] != curr: return False
                    heappop(hp)

        return True