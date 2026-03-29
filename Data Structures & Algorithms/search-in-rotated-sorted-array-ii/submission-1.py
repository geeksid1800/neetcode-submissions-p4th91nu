class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        An extension of #33.Search in Rotated Sorted Array.
        Consider a case like [1,1,1,1,0,1,1] and trying to find the minimum.
        m=3, nums[m] = 1, but when you compare to nums[-1], they are equal,
        so you have no idea whether you are in first or second sorted subarray - both
        have 1s in them. So you can't figure out whether to move left or right. 
        However, we can make a compromise. If nums[m]==nums[-1] and nums[m] != target,
        then nums[-1] != target as well. So we can remove nums[-1] from the search space.
        This is O(1), but we can gradually whittle down the search space till we can
        solve normally again.
        '''
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2

            if nums[m] == target:
                return True

            elif nums[m] == nums[r]:
                r -= 1 #since nums[m] != target, nums[r] != target as well. 

            elif nums[m] < nums[r]:
                # if nums[m] < nums[r], that means current m is part of the 
                # sorted right subarray. Now to figure out where we must look for target..
                if nums[m] <= target <= nums[r]:
                    # look in right of m
                    l = m+1
                else:
                    #look in left of m
                    r = m-1

            else:
                # nums[m] > nums[r], so current m is part of the sorted left subarray.
                # now to figure out where to look for target...
                if nums[l] <= target <= nums[m]:
                    #target is between them, so look left of m (guaranteed target != nums[m])
                    r = m-1
                else:
                    # look right of m
                    l = m+1
        
        return False

                
        