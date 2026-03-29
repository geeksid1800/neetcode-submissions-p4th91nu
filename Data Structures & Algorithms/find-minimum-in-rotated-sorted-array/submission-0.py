class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        We notice that elements before the minimum are larger than the last element in arr.
        Elements after the minimum are smaller than the last element in the arr.
        So aim is to find the first value smaller than arr[-1]
        '''
        l, r = 0, len(nums)-1
        ans = 0
        while l<=r:
            m = (l+r)//2
            if nums[m] <= nums[-1]:
                ans = nums[m] #possible answer
                r = m-1
            else:
                l = m+1
        return ans