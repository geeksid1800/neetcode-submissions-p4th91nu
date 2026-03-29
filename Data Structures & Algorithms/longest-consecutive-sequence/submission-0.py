class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        # for each num check if it is the start of a sequence by making sure
        # it's previous num is not in set
        ans = 0

        for num in nums: 
            if (num - 1) in s:
                continue
            else:
                #num is the first number of a sequence
                currCount = 0
                curr = num
                while curr in s:
                    currCount += 1
                    print(curr)
                    s.remove(curr)
                    ans = max(ans, currCount)
                    curr += 1
        
        return ans
