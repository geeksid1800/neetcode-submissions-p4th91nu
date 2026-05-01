'''
Since we visit each stn exactly once, whether we can make the ckt or not is wholly
determined by sum(gas) - sum(cost) >= 0. Once we know we can make it, we know there
is exactly 1 solution.
Create an arr diff[i] = gas[i]-cost[i]. Also maintain a running variable 'total'
tracking the total (gas-cost) we have available currently in our journey
If at any point total < 0, then we didn't pick the right starting point and gas ran
out. The next starting point should be the index after the one where you ran out,
and total is reset to 0. Logic: Say you started at ix 'i' and until j-1 you had
total>=0, and at j, you got total < 0 Then it doesn't make sense to start at any
'x' (i<=x<=j) as the sum(total) of [i:x] is +ve and by starting out at x, you miss
out on that much, which makes leaving j even harder.
Eg diff=[1(i),1,2,1(x),-1,-6(j),2,1]. We see that we accumulate total=4 until j-1
and it becomes -2 at j. By starting at x, we miss out on 1+1+2, and our total at j
becomes -6, so it makes no sense to start anywhere until after j (ie j+1).
Next, we start from the 'j+1'(2) and go to the end of the arr without running out.
We DON'T need to loop around for this starting point. This is because we already
tried all other ix as starting points except for 6 & 7 (i.e. 2 and 1) and none
of them were the answer, so it has to be one of these. Also if there is only 1 ans
then IT HAS TO BE ix=6 as it leads to an extra surplus of 2 compared to ix=7, ie
it's always better to start from ix=6 than ix=7 since diff[6] > 0.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) - sum(cost) < 0: return -1

        diff = [g-c for (g,c) in zip(gas,cost)]
        start, total = 0,0

        for i in range(n):
            if total < 0:
                start = i
                total = 0
            total += diff[i]
        
        return start