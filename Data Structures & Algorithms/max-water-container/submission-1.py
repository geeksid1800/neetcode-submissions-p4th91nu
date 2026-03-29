class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # for any i,j: vol = min(h[i],h[j]) * (j-i)
        # So we see that the limiting factor in the height is the smaller of
        # h[i] and h[j], so change the smaller one and hope for bigger volume.

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