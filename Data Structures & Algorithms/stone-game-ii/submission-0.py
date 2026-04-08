'''
1)Very similar to Stone Game I DP-approach. Instead of picking from both first and
last elements of piles, we only pick a variable number of piles from the front.
As a result, we don't need both (l,r) to track gamestate, rather an index i from
where we can start picking piles. This also means we can't directly infer whose
turn it is from the gamestate, and this will need to be passed as a parameter.
2) In previous case, we had two options at each turn, and needed to pick strictly
1 of them. Now we pick a variable no. of piles X from the front, 1<=X<=M, so M
needs to be a parameter too.
3) To decide the best X, we iterate through all possible options, picking the
optimal one. 
'''
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        #returns max Alice can score from this game state.
        def recur(AliceTurn,i,M):
            if i >= len(piles): return 0
            if (AliceTurn,i,M) in dp: return dp[(AliceTurn,i,M)]

            if AliceTurn:
                stones = 0
                res = 0
                for X in range(2*M):
                    '''
                    we are actually making X start from 0 so that i+X includes ith ix.
                    This means M is now decided by max(X+1,M)
                    '''
                    if i+X >= len(piles): break
                    stones += piles[i+X] #how many gained from this turn only
                    res = max(res, stones+recur(not AliceTurn,i+X+1,max(M,X+1)))

            else:
                res = float('inf')
                for X in range(2*M):
                    if i+X >= len(piles): break
                    res = min(res, recur(not AliceTurn,i+X+1,max(M,X+1)))
                    #no stones here as Alice does not gain anything in Bob's turn
            
            dp[(AliceTurn,i,M)] = res
            return res

        return recur(True,0,1)