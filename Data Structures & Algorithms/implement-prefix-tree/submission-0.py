class PrefixTree:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node[c] = node.get(c, dict())
            node = node[c]
        node['0'] = True #signals end of string
        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if node.get(c,None):
                nextNode = node[c]
                node = nextNode
            else:
                return False
        
        if node.get('0',None): #searching for 'do' when 'dog' is in trie doesn't give True
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if node.get(c,None):
                nextNode = node[c]
                node = nextNode
            else:
                return False
        
        return True
        