class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        RPN basically means postfix operations, where an operator acts upon
        the two nearest values to it's left.
        Traversing L->R, that means newer elements will get operated upon and added back
        to the same position, while older elements will wait for a future operator.
        This naturally implies a stack.
        '''
        stk = []
        for ele in tokens:
            if ele == '+':
                n1,n2 = stk.pop(), stk.pop()
                stk.append(n1+n2)
            elif ele == '-':
                n1,n2 = stk.pop(), stk.pop()
                stk.append(n2-n1)
            elif ele == '*':
                n1,n2 = stk.pop(), stk.pop()
                stk.append(n2*n1)
            elif ele == '/':
                n1,n2 = stk.pop(), stk.pop()
                stk.append(int(n2/n1))
            else:
                stk.append(int(ele))
            
        return stk[0]