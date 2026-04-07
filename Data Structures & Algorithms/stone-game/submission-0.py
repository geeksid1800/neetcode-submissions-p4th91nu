'''
There's a mathematical proof showing due to circumstances of problem and A getting
first pick, she can play so that she always has the choice of picking all odd ix
elements or all even ix elements. One of them will obviously be larger, so she
will calculate which and choose it, so guaranteeing her win. So soln is O(1).
However, dp-based soln is more generic and interesting, sharing that. 
NB:Greedy will not work. nums=[6,100,2,5]: If A chooses 6 greedily, it opens up 100
for B, guaranteeing his win. Instead if she chooses 5, she gets the 100 and wins.
1) This is a zero-sum game. Since total is fixed, Bob's objective of maximising
his own score is the same as him trying to minimize Alice's score during his own
turns.So in order for us to implement a soln with both playing optimally, we will
try to maximise A's scores during her turns, and minimize it during B's turns.
2) Let dfs(l,r) be the optimal Alice score with the subarray piles[l,r],i.e. after
some moves are played and we are left with that subarray. During the even numbered
turns Alice will play and during the odd # turns Bob will play.
3) During A's turn, she will have 2 choices, pick piles[l] or piles[r]. Her total
optimal score from then on will be given by max(piles[l]+dfs(l+1,r), piles[r]+
dfs(l,r-1)).
During B's turn, not only will A not earn anything in that turn, B will choose the
available option that will minimize A's score.
So dfs(l,r) = 0+min(dfs(l+1,r),dfs(l,r-1)) signifying the best case for what Alice
can earn when that is the game state.
In the end, if Alice has scored more than total/2 in the whole game, she wins.
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        #Returns: the maximum Alice can score from the subarray piles[l,r]
        def dfs(l, r):
            if l > r: return 0
            if (l,r) in dp: return dp[(l,r)]
            AliceTurn = True if (r-l)%2 else False

            # in bob's turn, he chooses the option which minimizes alice's score
            if not AliceTurn:
                dp[(l,r)] = min(dfs(l+1, r), dfs(l, r-1))
                return dp[(l,r)]

            #Alice has two choices: choose leftmost or rightmost pile.
            dp[(l,r)] = max(dfs(l+1, r) + piles[l], dfs(l, r-1) + piles[r])
            return dp[(l,r)]

        aliceMaxScore = dfs(0, len(piles)-1)
        return aliceMaxScore > sum(piles)//2