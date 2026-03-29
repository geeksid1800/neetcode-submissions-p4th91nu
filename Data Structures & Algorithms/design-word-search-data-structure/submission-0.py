class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node[c] = node.get(c, dict())
            node = node[c]

        node['0'] = True

    def search(self, word: str) -> bool:
        def recur(node, i):
            if i == len(word):
                return True if '0' in node else False
            c = word[i]
            if c == '.':
                for avl in node:
                    if (avl != '0') and recur(node[avl],i+1):
                        return True
                return False
            elif c in node:
                return recur(node[c],i+1)
            else:
                return False
        
        return recur(self.root, 0)
            