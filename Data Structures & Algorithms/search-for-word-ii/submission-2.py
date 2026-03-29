'''
DFS + Trie + Backtracking based solution. 
Things to remember is "back" and "backend" can both be words, so don't stop looking after you find a 0
Also, the same word can be formed from two different paths, so if you find a '0' remove it from the 
Trie, so the next time we find the same word, it's not added to answer again.
'''
class Trie:
    def __init__(self):
        self.root = dict()
    def insert(self, word) -> None:
        curr = self.root
        for c in word:
            curr[c] = curr.get(c, dict())
            curr = curr[c]
        curr['0'] = True
    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True if '0' in curr else False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        used = set()
        ans = []
        trie = Trie()
        m,n = len(board), len(board[0])
        for word in words:
            trie.insert(word)

        def dfs(r, c, curr, trieNode):
            if '0' in trieNode:
                #we have reached one complete word, add it to answer
                #we also continue if we can, e.g. if "back" and "backend" both in words
                ans.append("".join(curr))
                #remove this word from coming twice if it can be formed another way
                trieNode.pop('0')
            if r>=m or r<0 or c>=n or c<0 or (r,c) in used:
                return
            ch = board[r][c]
            if ch not in trieNode:
                '''the Trie does not have that particular letter at this point in any word.
                Eg. if board[0][0] is 'a' and no valid word starts with 'a', then trie[a]
                will not exist. So we straightaway know this route is pointless.'''
                return
            nextNode = trieNode[ch]

            used.add((r,c))
            curr.append(ch)

            dfs(r+1,c, curr, nextNode)
            dfs(r-1,c, curr, nextNode)
            dfs(r, c+1, curr, nextNode)
            dfs(r, c-1, curr, nextNode)

            used.remove((r,c))
            curr.pop()
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, [], trie.root)
        return ans