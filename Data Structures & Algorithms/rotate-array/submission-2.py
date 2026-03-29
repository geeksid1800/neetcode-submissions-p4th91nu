class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Eg [1,2,3,4,5], k = 2 -> [(4,5),(1,2,3)]
        # Notice reverse(nums) is  [(5,4),(3,2,1)]
        # The individual groups are in the right places, we just have to fix
        # within a group.

        n = len(nums)
        k = k%n #for cases where k is larger than n

        def rev_subgroup(start, end) -> None:
            l = start
            r = end
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return 
        
        nums.reverse()
        rev_subgroup(0,k-1)
        rev_subgroup(k, n-1)