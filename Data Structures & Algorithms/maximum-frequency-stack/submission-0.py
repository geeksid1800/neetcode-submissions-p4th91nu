class FreqStack:

    def __init__(self):
        self.value_counts = {} #stores the count of each unique value
        self.frequencies = {} #stores all elements with that frequency in a list
        self.max_count = 0

    def push(self, val: int) -> None:
        self.value_counts[val] = self.value_counts.get(val,0) + 1
        currcount = self.value_counts[val]
        self.max_count = max(self.max_count, currcount)

        self.frequencies[currcount] = self.frequencies.get(currcount, [])
        self.frequencies[currcount].append(val)
        #store 'val' in the list that has hashmap key as the current count of 'val'

    def pop(self) -> int:
        val = self.frequencies[self.max_count].pop()
        self.value_counts[val] -= 1
        if not self.frequencies[self.max_count]: #no more elements with that count
            self.max_count -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()