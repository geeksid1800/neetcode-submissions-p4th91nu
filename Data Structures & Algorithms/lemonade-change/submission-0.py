'''
Although this qn can be solved using DFS, we can solve it much more simply in O(n)
using a greedy approach based on the following ideas:
1) 20 is never useful as change, as the max change reqd will be 15
2) 5s are more useful than 10s, as you can pay off 15 with 3 5s or (5+10), but you
can't pay off 5 change with a 10.
So the priority order is 5>10>20 bills.
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0,0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                if fives: fives -= 1
                else: return False
            else:
                if fives and tens:
                    fives -=1; tens -=1
                elif fives>=3:
                    fives -=3
                else: return False
        
        return True