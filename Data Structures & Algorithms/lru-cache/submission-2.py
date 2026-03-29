'''
Default Least Recently Used structure implies FIFO - queue. But the issue is moving an
arbitrary key from the middle of the queue to the end when it is accessed, in O(1).
This implies we need to use a Linked List, instead of an array, and we also need a way
to find/lookup the key in O(1), implying we need to maintain a hashmap of nodes.
Also, when a particular node is plucked and moved to the end, the node that was prior
now needs to point to the node that was after it, so we need a way to know the previous
node for any arbitrary node => Doubly linked list.
'''
class ListNode:
    def __init__(self, key: int = -1, val: int = -1, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap, self.count = capacity, 0
        self.root = ListNode()
        self.tail = ListNode()
        self.root.next, self.tail.prev = self.tail, self.root
        self.cache = {} # key:node mapping

    def remove(self, key: int) -> None:
        # given a key, removes the node with that key from the LL, cache
        if not self.cache.get(key, None):
            return
        delNode = self.cache[key]
        prevNode, nextNode = delNode.prev, delNode.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        self.cache.pop(key)
        del delNode
    
    def addToEnd(self, key: int, value: int) -> None:
        # moves a recently accessed node to the end of the LL
        if self.cache.get(key, None):
            self.remove(key)
        newNode = ListNode(key, value, None, None)
        oldLast = self.tail.prev
        oldLast.next = self.tail.prev = newNode
        newNode.prev, newNode.next = oldLast, self.tail
        self.cache[key] = newNode


    def get(self, key: int) -> int:
        if not self.cache.get(key,None):
            return -1
        val = self.cache[key].val
        self.remove(key)
        self.addToEnd(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        #if key already exists, remove the old node with that key
        #always add a new node with the key to the end of the LL
        #after adding, if you exceed capacity, remove leftmost node
        if self.cache.get(key,None):
            self.remove(key)
            self.count -= 1

        self.count += 1
        self.addToEnd(key, value)

        if self.count > self.cap:
            #remove the leftmost node
            oldestKey = self.root.next.key
            self.count -= 1
            self.remove(oldestKey)
   