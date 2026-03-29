'''
eject the smallest elements in arr until there are only k elements left
Then the smallest element will be Kth largest
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]