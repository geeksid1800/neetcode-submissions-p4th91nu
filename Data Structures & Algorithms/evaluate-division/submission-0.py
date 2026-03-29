from collections import defaultdict
'''In general, for each disjoint set, all vars will be expressed in terms of the root var. 
For eg, if c is the root of a DSU whose other members are a and b, and a/b=3 and b/c=2,
then we will store in the DSU's nodes [a,6], [b,2] and [c,1] as a=6c, b=2c, and c=1c.'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        expr = {} # {a -> [b,3]} means a = 3b or a/b = 3
        def find_root(var):
            '''If var is not defined in terms of itself (i.e. [var,1]), it is part of a bigger tree.
            In that case, find the root and var's ratio when compared to the root (i.e. [root,wt])'''
            den, nums_ratio_to_den = expr.get(var, [var,1])
            if var == den:
                expr[var] = [den,1]
                return expr[var]
            #denominator is expressed in terms of some other var, find out that var and so on
            root, dens_ratio_to_root = find_root(den)
            expr[var] = [root, nums_ratio_to_den*dens_ratio_to_root]
            return expr[var]
        
        def union(a,c,k):
            '''
            Eg.Let a/b = 2 already; now we are told a/c = 3. So a=[b,2] is already done and c=[c,1]
            Since root of a is b and root of c is c, they are different and we need to reconcile.
            a=r_a*w_a, c=r_c*w_c and a/c=k => (r_a*w_a)/(r_c*w_c) = k => r_a = (k*w_c/w_a)*r_c
            So redefine r_a = [r_c, k*w_c/w_a] i.e. b=[c,3/2]
            '''
            r_a, w_a = find_root(a)
            r_c, w_c = find_root(c)
            if r_a != r_c:
                expr[r_a] = [r_c, (k*w_c)/w_a]
        
        
        for (num,den), ratio in zip(equations, values):
            union(num,den,ratio)
        
        ans = []
        for num,den in queries:
            if num not in expr or den not in expr:
                ans.append(-1.0)
                continue
            r_num, w_num = find_root(num)
            r_den, w_den = find_root(den)
            if r_num != r_den: #no way to find a relation between them
                ans.append(-1)
            else:
                ans.append(w_num/w_den)
        
        return ans
