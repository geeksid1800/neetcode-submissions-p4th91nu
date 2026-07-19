'''
The Dutch National Flag algorithm partitions the array into three sections 
in a single pass. We maintain pointers for the boundary of 0s (left), 
the boundary of 2s (right), and the current element being examined. 
When we see a 0, we swap it to the left section. When we see a 2, we swap it 
to the right section. 1s naturally end up in the middle.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l,r,i = 0,n-1,0 #0s:[0,l-1] and 2s:[r+1:]
        while i<=r: #if we get a section of just 2s, we'll be stuck infinitely
            if nums[i] == 0:
                #move it into the leftmost partition, whose size increases
                nums[l],nums[i] = nums[i], nums[l]
                l, i = l+1, i+1
            elif nums[i] == 2:
                #move it into the rightmost partition, whose size increases
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                #don't increment i, we don't know what value we got into it rn
                #so we still need to process that again
            else:
                i += 1
        
