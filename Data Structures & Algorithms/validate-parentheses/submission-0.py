from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        for c in s:
            if c in ('(','{','['):
                st.append(c)
            elif len(st) == 0:
                return False
            else:
                top = st.pop()
                if c == ')' and top != '(':
                    return False
                if c == '}' and top != '{':
                    return False
                if c == ']' and top != '[':
                    return False
        
        if len(st):
            return False
        
        return True