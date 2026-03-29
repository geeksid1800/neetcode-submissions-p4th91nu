class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for curr in asteroids:
            while len(stk)>0 and stk[-1] > 0 and curr < 0: #collision (possibly multiple)
                top = stk[-1]
                if abs(curr) > abs(top):
                    stk.pop()
                elif abs(curr) == abs(top):
                    curr = 0 #both destroyed
                    stk.pop()
                else:
                    curr = 0
            
            if abs(curr) > 0:
                # curr survives all collisions it faces
                stk.append(curr)
        
        return stk
