class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        maxL = [0 for _ in range(n)]
        maxR = [0 for _ in range(n)]

        for i in range(1,n):
            maxL[i] = max(maxL[i-1], height[i-1]) #max height to the left of i
            maxR[n-1-i] = max(maxR[n-i], height[n-i]) #max height to right of i

        for i in range(0,n):
            if height[i] < maxL[i] and height[i] < maxR[i]:
                #water will be above a tower only if it has towers
                #taller than it on both sides
                vol = min(maxL[i], maxR[i]) - height[i]
            else:
                vol = 0
            ans += vol
        
        return ans
