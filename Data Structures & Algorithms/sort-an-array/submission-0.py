def sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    left = sort(nums[:mid])
    right = sort(nums[mid:])
    ans = []
    p1 = p2 = 0
    while (p1<len(left) and p2<len(right)):
        if left[p1] < right[p2]:
            ans.append(left[p1])
            p1 += 1
        else:
            ans.append(right[p2])
            p2 += 1
    if p1 < len(left):
        ans.extend(left[p1:])
    if p2 < len(right):
        ans.extend(right[p2:])
    return ans

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sort(nums)