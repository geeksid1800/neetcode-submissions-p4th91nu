from collections import deque

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()

        for c in operations:
            if c == '+':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.extend([n1,n2,n1+n2])
            elif c == 'D':
                n1 = stack.pop()
                stack.extend([n1, 2*n1])
            elif c == 'C':
                stack.pop()
            else:
                stack.append(int(c))
        
        ans = 0
        while len(stack):
            ans += stack.pop()

        return ans