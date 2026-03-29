class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        In first pass, implement the generic element:count hashmap
        In second pass, use the previous hashmap to build a new hashmap/array
        This one will have count as index and list of elements with that count as val
        Then just simply iterate from the largest to smallest counts to get k elements

        The good part is if we have total 'n' elements in nums, we need an array
        of size n+1 (at max) for second pass, 
        irrespective of size of elements themselves.
        """
        m1 = {}
        for n in nums: 
            m1[n] = m1.get(n,0) + 1

        ans = []
        elements = [[] for i in range(len(nums)+1)]

        for ele, cnt in m1.items():
            elements[cnt].append(ele)
        
        
        for counts in elements[::-1]:
            if len(ans) >= k:
                return ans
            ans.extend(counts)
        
        return ans