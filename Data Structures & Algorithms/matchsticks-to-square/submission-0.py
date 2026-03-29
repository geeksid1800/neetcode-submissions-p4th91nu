from collections import Counter
'''
Go on building side by side of the square with what matchsticks you have left. If there is a soln, Length of sides is already known (total/4). When you have finished building current side (remaining length of
current side is 0), move on to the next side. 
At each point, iterate through all available matchsticks, and try to build a solution with all of the
sticks <= remaining side length.  
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        if tot%4: return False
        matchsticks.sort(reverse=True)
        length = tot//4
        if matchsticks[0] > length: return False
        cnt = Counter(matchsticks)

        def recur(side, cnt, rem):
            #Currently trying to build side no. 'side' of which 'rem' is left to be built,
            #available matchsticks are in cnt

            if not rem:
                #move on to next side
                return recur(side+1,cnt,length)

            if side==5:
                if cnt:
                    return False
                return True

            #iterate through available matchsticks and try to make a solution with it
            ans = False
            for stick in cnt:
                if stick <= rem:
                    ans = ans or recur(side, cnt-Counter([stick]), rem-stick)
            
            return ans
        
        return recur(side=1, cnt=cnt, rem=length)
