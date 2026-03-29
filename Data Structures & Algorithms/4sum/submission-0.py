class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we will solve for a generalised k-Sum (k>2)
        nums.sort()
        ans, curr = [],[]
        def kSum(k, start, target):
            if k == 2:
                # Just two-sum when k reaches 2
                l, r = start, len(nums)-1

                while l<r:
                    twoSum = nums[l] + nums[r]
                    if twoSum < target:
                        l += 1
                    elif twoSum > target:
                        r -= 1
                    else:
                        ans.append(curr + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                        while l<r and nums[r] == nums[r+1]:
                            r -= 1
                return

            for i in range(start, len(nums)-k + 1):
                if (i>start) and (nums[i] == nums[i-1]):
                    continue
                curr.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                curr.pop()


        kSum(4, 0, target)
        return ans
