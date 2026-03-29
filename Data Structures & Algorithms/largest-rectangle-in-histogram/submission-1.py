class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        For each bar, find the first bar on the left and the right, that are shorter
        than the current bar. 
        Use that to find the last consecutively greater than equal bar on left/right
        '''
        n = len(heights)
        leftstk, rtstk = [], []
        fsel = [-1 for i in range(n)]
        fser = [n for i in range(n)] #first smaller element left/right

        for ix, height in enumerate(heights):
            while leftstk and heights[leftstk[-1]] >= height:
                leftstk.pop()
            if leftstk:
                fsel[ix] = leftstk[-1]
            leftstk.append(ix)

        for ix in range(n-1,-1,-1):
            height = heights[ix]
            while rtstk and heights[rtstk[-1]] >= height:
                rtstk.pop()
            if rtstk:
                fser[ix] = rtstk[-1]
            rtstk.append(ix)

        ans = 0
        for ix, ht in enumerate(heights):
            width = (fser[ix] - 1) - (fsel[ix] + 1) + 1
            #last bigger index on right is fser[ix]-1, on left is fsel[ix]+1
            ans = max(ans, ht*width)

        return ans
        
