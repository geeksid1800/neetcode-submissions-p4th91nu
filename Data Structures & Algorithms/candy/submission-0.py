'''
Two-pass approach
First pass: Go left to right, making sure that candies[i] > candies[i-1] if
ratings[i]>ratings[i-1] for all i
Second pass: Go right to left, making sure that candies[i]>candies[i+1] if
ratings[i]>ratings[i+1] for all i
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i-1]+1,candies[i])
        
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1]+1,candies[i])
        
        return sum(candies)