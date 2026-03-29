from collections import defaultdict, deque
'''
The complicated part here is building the adjacency list for each word. After that, it is a simple
BFS to find shortest path from source to target.
For building adj, we will consider replacing one position of our current word with *:
ie bat becomes *at, so it can match patterns of cat, hat etc. We repeat this with wildcard being 
every single position on word. We create a hashmap of pattern:list for each pattern, and add all
words matching that pattern to it's corresponding list. ie patterns[*at] = [hat, bat, cat..],
patterns[b*t] = [bat, bet, bit...]
Then, we create adj for each word in patterns[pattern] by adding all other words in the same list,
as it's neighbors. Eg neighbors of bat are hat, cat, bet, bit...
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj, patterns = defaultdict(list), defaultdict(list)
        visited = set()
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        for words in patterns.values():
            for wordIx, word in enumerate(words):
                adj[word].extend(words[:wordIx]) #insert all words except word itself, as neighbors
                adj[word].extend(words[wordIx+1:]) #of word, in adjacency list

        q = deque([beginWord])
        ans = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return ans
                visited.add(word)
                for nbr in adj[word]:
                    if nbr not in visited: q.append(nbr)
            ans += 1
        return 0

