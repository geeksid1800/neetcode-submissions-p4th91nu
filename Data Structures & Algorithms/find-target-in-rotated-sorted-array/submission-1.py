class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Basically an extension of #153. Find Minimum in Rotated Sorted Array.
        First find the minimum, and then binary search either on the left or the right,
        since both are sorted arrays in themselves.
        '''
        l, r = 0, len(nums)-1
        minE = 0
        while l<=r:
            m = (l+r)//2
            if nums[m] <= nums[-1]:
                minE = m #potentially the minimum in array
                r = m-1
            else:
                l = m+1
        
        if target <= nums[-1]:
            #check in the right subarray
            l, r = minE, len(nums)-1
            while l<=r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    return m
            return -1

        else:
            #check in the left subarray
            l, r = 0, minE-1
            while l<=r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    return m
            return -1