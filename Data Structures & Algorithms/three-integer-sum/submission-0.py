class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if (i>0 and (nums[i] == nums[i-1])):
                continue
            
            l, r = i+1, len(nums)-1
            while(l<r):
                threeSum = nums[l] + nums[r] + num
                if (threeSum == 0):
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (l<r and nums[l] == nums[l-1]):
                        l += 1
                    while (l<r and nums[r] == nums[r+1]):
                        r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return ans