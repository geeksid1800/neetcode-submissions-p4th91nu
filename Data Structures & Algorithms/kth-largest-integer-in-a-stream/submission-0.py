from heapq import heapify, heappop, heappush #creates and maintains MIN-HEAP

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        while len(self.nums) > k:
            heappop(self.nums)
            '''left only with the k biggest elements after this,
               so smallest element in array is kth largest element'''

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]