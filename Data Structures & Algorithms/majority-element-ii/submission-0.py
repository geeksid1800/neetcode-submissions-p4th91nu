class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = None, None #there are at max two possible elements as answers
        v1, v2 = 0,0 #No. of votes for each candidate

        for num in nums:
            if c1 == num:
                v1 += 1
            elif c2 == num:
                v2 += 1
            elif v1 == 0:
                c1 = num
                v1 = 1
            elif v2 == 0: 
                c2 = num
                v2 = 1
            else:
                v1 -= 1
                v2 -= 1
            
        thresh = (len(nums)//3) + 1
        # we only got the most common elements, we don't know if they're truly majority
        # Eg. [3,5,5,5,5,5] would give c1 = 3, c2 = 5, but 3 is not a majority element
        return [n for n in (c1,c2) if nums.count(n) >= thresh]