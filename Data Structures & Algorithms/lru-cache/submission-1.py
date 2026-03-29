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
    def __init__(self, key:int = 0, val: int = 0, prev = None, next = None):
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

    def get(self, key: int) -> int:
        if not self.cache.get(key,None):
            return -1
        Node = self.cache[key]
        oldPrev, oldNext = Node.prev, Node.next
        oldPrev.next, oldNext.prev = oldNext, oldPrev
        oldLast = self.tail.prev
        oldLast.next = self.tail.prev = Node
        Node.prev, Node.next = oldLast, self.tail
        return Node.val 

    def put(self, key: int, value: int) -> None:
        #if key already exists, remove the old node with that key
        #always add a new node with the key to the end of the LL
        #after adding, if you exceed capacity, remove leftmost node
        if self.cache.get(key,None):
            Node = self.cache[key]
            Node.val = value
            oldPrev, oldNext = Node.prev, Node.next
            oldPrev.next, oldNext.prev = oldNext, oldPrev
            oldLast = self.tail.prev
            oldLast.next = self.tail.prev = Node
            Node.prev, Node.next = oldLast, self.tail
        else:
            newNode = ListNode(key, value, None, None)
            self.count += 1
            self.cache[key] = newNode
            oldLast = self.tail.prev
            oldLast.next = self.tail.prev = newNode
            newNode.prev, newNode.next = oldLast, self.tail

        if self.count > self.cap:
            #remove the leftmost node
            delNode = self.root.next
            self.count -= 1

            if delNode != self.tail:
                self.cache.pop(delNode.key)
                newFirst = delNode.next
                self.root.next, newFirst.prev = newFirst, self.root
                del delNode        
   
