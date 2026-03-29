'''
maintain two heaps to store the left and right sides of the median, respectively.
Maintain a max difference of 1 between the sizes of the heaps at any point.
Left side should be max-heap, so we can pop the largest element and move it to the right.
Conversely, right side should be min-heap
'''
class MedianFinder:

    def __init__(self):
        self.left, self.right = [],[]
    
    def rebalance(self) -> None:
        while len(self.left) > len(self.right) + 1:
            #left is max-heap, elements are made negative; right is min-heap
            mid = -1*(heapq.heappop(self.left))
            heapq.heappush(self.right, mid)
        
        while len(self.right) > len(self.left) + 1:
            mid = -1*(heapq.heappop(self.right))
            heapq.heappush(self.left, mid)

    def addNum(self, num: int) -> None:
        if self.right and num >= self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        self.rebalance()    

    def findMedian(self) -> float:
        if (len(self.left)+len(self.right))%2:
            if len(self.left)>len(self.right):
                return float(-self.left[0]) #largest on left side
            else:
                return float(self.right[0]) #smallest on right side
        
        else:
            #if sum of lengths is even, both sides must have equal numbers
            return (-self.left[0] + self.right[0])/2.0