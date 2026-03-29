class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        '''
        We notice that as soon as the array becomes increasing in any subarray,
        we get the answer for the elements in that subarray. 
        i.e if 31 is in array, and 32 is next day, we get answer for 31 and all
        previous elements less than 32.
        Hence, at any point, we are maintaining a monotonic decreasing array of elements
        and popping all elements smaller than curr from the end as long as possible,
        and finally adding curr to the end.
        This naturally implies a stack - removing and adding both from the end
        '''
        stk = []
        ans = [0] * len(temp)
        
        for ix,curr in enumerate(temp):

            while len(stk) and curr > temp[stk[-1]]:
                '''store indexes in stack instead of values themselves
                #that way we can easily find the gap between current day
                and the day it is hotter than '''
                ans[stk[-1]] = ix - stk[-1]
                stk.pop()

            stk.append(ix)

        return ans