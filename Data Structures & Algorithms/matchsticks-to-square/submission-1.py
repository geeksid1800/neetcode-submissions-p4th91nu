from collections import Counter
'''
Recursive function takes as argument i'th matchstick and puts it along one of the sides.
If you can, and also put the next one and so on, answer is True.
Otherwise answer is True.
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        if tot%4: return False
        matchsticks.sort(reverse=True)
        length = tot//4
        if matchsticks[0] > length: return False
        sides = [0]*4

        def recur(i): #tries to put matchsticks[i] in one of the sides
            if i == len(matchsticks):
                return True #put all the matchsticks successfully in one of the sides
            
            for j in range(4): #each of the 4 possible sides
                if sides[j]+matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if recur(i+1):
                        return True
                    sides[j] -= matchsticks[i]

            return False #could not find anywhere to put current matchsticks[i]

        return recur(0)
