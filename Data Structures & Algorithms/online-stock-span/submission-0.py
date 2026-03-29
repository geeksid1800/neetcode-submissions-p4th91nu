'''Given the example: [100, 80, 60, 70, 60, 75, 85].
If we need to calculate the span for an element that is smaller than it's previous ele, 
(Eg. 80), it is quite trivially 1. 
How to calculate the span for an element >= it's previous element (eg. 75, 85)
Let's say we have calculated the spans for all elements up till 75 ->
spans array looks like [1, 1, 1, 2, 1, 4], now we need to calculate span for 85..
We observe that any element smaller than 75 will also be smaller than 85, so span of 85
is atleast 5 (it's own 1 + 4 from '75') as it is >= 60, 70, 60, 75, 85.
So from comparing with 75, we can directly jump backwards to the first element bigger than
75, which is behind 4 places (as 75's span is 4)..i.e we compare now with 80.
We keep repeating this process until we either find current element to be bigger than ALL
previous elements in array, or we find an element back there which is bigger than curr. 
'''

class StockSpanner:

    def __init__(self):
        self.spans = []

    def next(self, price: int) -> int:
        if len(self.spans) == 0:
            self.spans.append({"price":price, "span":1})
            return 1
        
        candidate = len(self.spans)-1 #ix of candidate element to compare against 'price'
        #candidate is initially the latest element in spans array (i.e. yesterday)
        ans = 1
        while candidate >= 0 and self.spans[candidate].get("price") <= price:
            ans += self.spans[candidate].get("span")
            candidate -= self.spans[candidate].get("span")
        
        self.spans.append({"price":price, "span":ans})
        return ans



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)