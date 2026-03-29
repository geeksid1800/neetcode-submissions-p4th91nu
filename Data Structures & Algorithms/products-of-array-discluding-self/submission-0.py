class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preproduct = [1]*n #will store product of every num before current
        postproduct = [1]*n #will store product of every num after current

        for i in range(1,n):
            preproduct[i] = preproduct[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            postproduct[i] = postproduct[i+1] * nums[i+1]

        ans = [1]*n
        for i in range(n):
            ans[i] = preproduct[i] * postproduct[i]
        return ans
