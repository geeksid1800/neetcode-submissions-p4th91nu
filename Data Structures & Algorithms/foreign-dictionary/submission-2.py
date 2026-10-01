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
        #step 1: build the adjacency sets (sets instead of lists to prevent duplicate letters)
        adj = {char:set() for word in words for char in word}
        
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            len2 = len(w2)
            if len2<len(w1) and w1[:len2] == w2: return "" #w2 is a prefix of w1 but comes after it.
            for j in range(min(len(w1), len(w2))):
                if w1[j] == w2[j]: continue
                adj[w1[j]].add(w2[j]) #the first char where w1 and w2 mismatch
                break
        
        visiting, visited = set(), set()
        ans = []
        def dfs(char) -> bool: #returns True if char can successfully be ordered, False otherwise
            if char in visiting: return False #cycle detected. a before b but also b before a
            if char in visited: return True #char is already added to toposort answer

            visiting.add(char)
            for child in adj[char]:
                if not dfs(child): #child was part of a cycle
                    return False
            visiting.remove(char); visited.add(char)
            ans.append(char) #classic postorder traversal in Toposort. add char only after all childs
            return True
        
        for char in adj:
            if not dfs(char): return ""
        return "".join(reversed(ans))