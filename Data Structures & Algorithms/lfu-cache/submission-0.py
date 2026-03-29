class ListNode:
    def __init__(self, key = -1, value = -1, next = None, prev = None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev
        self.uses = 0

class LinkedList:
    #each count has it's own LL, e.g. all elements accessed once are in the same LL
    def __init__(self):
        self.root = ListNode()
        self.tail = ListNode()
        self.root.next, self.tail.prev = self.tail, self.root
        self.nodeMap = dict() #key:ListNode
    
    def length(self):
        #return number of nodes in LL
        return len(self.nodeMap)
    
    def addToEnd(self, key, val):
        oldLast = self.tail.prev
        node = ListNode(key=key, value = val, next = self.tail, prev = oldLast)
        oldLast.next = self.tail.prev = node
        self.nodeMap[key] = node
    
    def remove(self, key):
        if key not in self.nodeMap:
            return
        delNode = self.nodeMap[key]
        oldLeft, oldRight = delNode.prev, delNode.next
        oldLeft.next, oldRight.prev = oldRight, oldLeft
        self.nodeMap.pop(key)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minCount = 0 #the access count of the least accessed key(s)
        self.valMap = dict() #key: val
        self.countMap = dict() #count: LL for that particular count
        self.keyCount = dict() #key: count
    
    def updateCount(self, key):
        #whenever a key is accessed, this method should be called to handle all updates
        cnt = self.keyCount.get(key,0)
        self.keyCount[key] = cnt + 1
        oldLL = self.countMap.get(cnt, LinkedList())
        oldLL.remove(key)
        newLL = self.countMap.get(cnt+1, LinkedList())
        newLL.addToEnd(key, self.valMap[key])
        self.countMap[cnt], self.countMap[cnt+1] = oldLL, newLL

        #if oldLL is empty, that means no keys with that count exist anymore =>
        #there is a possibility that the minimum count has changed, update if needed
        if oldLL.length() == 0 and self.minCount == cnt:
            self.minCount += 1 #old minCount was cnt itself, and now no keys with that count

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        val = self.valMap[key]
        self.updateCount(key)
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        #we may only exceed capacity if we are adding a new key
        if key not in self.valMap and len(self.valMap) == self.cap:
            #remove the leftmost node in the least used count's LL
            minLL = self.countMap[self.minCount]
            firstKey = minLL.root.next.key
            minLL.remove(firstKey)
            self.valMap.pop(firstKey)
            self.keyCount.pop(firstKey)
        
        self.valMap[key] = value
        self.updateCount(key)
        self.minCount = min(self.minCount, self.keyCount[key])

            
        
            
