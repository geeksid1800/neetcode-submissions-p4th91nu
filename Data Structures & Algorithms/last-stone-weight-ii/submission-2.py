'''
Greedy approach doesn't work, refer notes for counterexample.
Instead what we need to do is divide stones into 2 bags/groups, which we will try
to make as close as possible in weight to each other. Then, we smash rocks from
opposite bags into each other, achieving the optimal score.
Eg. [2,7,4,1,8,1] => [7,4] and [2,1,8,1] => The difference after smashing is 1.
Basically, we need to divide stones into group1 and group2 and minimise the
difference between them, abs(sum(grp1)-sum(grp2)). This now becomes a simple
problem of choosing whether to pick stone[i] in grp1 or not, which we can solve
recursively.
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot = sum(stones)
        dp = {}

        def recur(i,sum1):
            '''
            returns the minimal difference between the two groups created so far.
            i: ix of element we are choosing to group right now.
            sum1: the current (cumulative) sum of group 1.
            '''
            if i==len(stones):
                return abs(sum1 - (tot-sum1))
            if (i,sum1) in dp: return dp[(i,sum1)]

            #we have 2 options: include or don't stones[i] in group1
            dp[(i,sum1)] = min(recur(i+1,sum1+stones[i]), recur(i+1,sum1))
            return dp[(i,sum1)]

        return recur(0,0)