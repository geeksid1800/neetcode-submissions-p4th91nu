class Solution:
    def decodeString(self, s: str) -> str:
        '''
        It is apparent that we should solve for any subproblems first, i.e. solve inside to
        outwards. For that, we notice that the innermost ']' occurs first in the array.
        Hence, we keep adding elements to the array until we encounter a ].
        the latest (i.e. innermost) [ will have a number before it as well, so we
        track back until we reach the [ to get the string to multiply and then back a
        few steps more to get how many times to repeat it. We then add k*substr that we
        just calculated to the stack (as outer multiples will also need this decoded substr)
        and repeat. Since we are taking the innermost decoded substring from the end,
        and adding it's decoded version back to the end, we use a stack.  
        '''
        stk = []
        for i in range(len(s)):
            c = s[i]
            if c == ']':
                substr = []
                while stk[-1] != '[':
                    substr.append(stk.pop()) #substr consists of everything b/w [ and ]
                substr = "".join(substr[::-1])
                stk.pop() #remove the [
                k = []
                while stk and stk[-1].isdigit(): # before [ comes k
                    k.append(stk.pop())
                k = int("".join(k[::-1]))

                stk.append(k*substr) # add the newly decoded substring back to stack
                #outer encodings (if any) will use it next. 
            else:
                stk.append(c)
            
        return "".join(stk)