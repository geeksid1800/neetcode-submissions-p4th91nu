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
        if len(words) == 1: return words[0]
        adj = {c:set() for word in words for c in word}
        for first, second in zip(words,words[1:]):
            length = min(len(first), len(second))
            for ix in range(length):
                if first[ix] == second[ix]:
                    if ix==len(second)-1 and len(second)<len(first):
                        return "" #second is a prefix of first, invalid ordering
                    else: continue
                adj[first[ix]].add(second[ix])
                break #we continue only till the first mismatch

        visiting, visited = set(), set()
        ans = []
        def dfs(char) -> bool:
            #returns True if char (along with its successors) can be logically ordered, else False
            if char in visiting: return False #cycle detected
            if char in visited: return True #char is already in the toposort ordering
            visiting.add(char)
            for child in adj[char]:
                if not dfs(child):
                    #child cannot be ordered, so neither can this
                    return False
            visiting.remove(char)
            visited.add(char)

            #toposort: add char only after all it's children's dependencies are themselves resolved
            ans.append(char)
            return True
        
        #now do a toposort for each component, so that relative ordering within component is correct
        for char in adj:
            if not dfs(char): return ""
        return "".join(reversed(ans))
