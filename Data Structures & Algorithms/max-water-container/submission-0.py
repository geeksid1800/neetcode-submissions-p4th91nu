class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i, j = 0, len(heights) - 1

        while i<j:
            curr = min(heights[i], heights[j]) * (j-i)
            ans = max(curr, ans)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return ans