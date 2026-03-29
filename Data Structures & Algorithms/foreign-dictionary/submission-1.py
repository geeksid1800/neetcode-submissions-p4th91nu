'''
An ordering/list of words will be invalid in two cases:
1) A clearly lexicographically larger string before a smaller one. Eg. 'apes' comes before 'ape'.
2) The ordering forms a cycle. Eg. we see s<d but also separately d<f<g<s
If we observe either of these, immediately return "". Otherwise, do pairwise comparison of every
two distinct characters in every consecutive pair of words, and build an adjacency set if a char
a is before b as adj[a] = b. Then, do a topological sort of all the characters in our adj set.
Eg d<f<g<h and t<y<u in our adj sets, then we do postorder traversal as is normal in TopoSort.
'''
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #set instead of list to prevent duplicate children
        adj = {c:set() for word in words for c in word}
        
        if len(words) > 1:
            for i in range(1, len(words)):
                w1, w2 = words[i-1], words[i]
                len2 = len(w2)
                if len(w1) > len2 and w1[:len2] == w2: return "" #invalid ordering
                for j in range(min(len(w1), len(w2))):
                    if w1[j] == w2[j]: continue
                    adj[w1[j]].add(w2[j]) #w2[j] is after w1[j] in the alien language
                    break
        
        visited, visiting = set(), set()
        ans = []
        def dfs(char):
            '''Function returns false if we detect a loop,
            Otherwise, it does topological sort of the DAG and returns True
            '''
            if char in visiting:
                return False #invalid DFS (found cycle)
            if char in visited:
                return True #char has already been added to our toposort ans
            
            visiting.add(char)
            for nxt in adj[char]:
                if not dfs(nxt): #nxt is part of a cycle
                    return False
            
            visiting.remove(char)
            visited.add(char)
            ans.append(char) #postorder traversal in topo-sort
            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        
        return "".join(ans[::-1])