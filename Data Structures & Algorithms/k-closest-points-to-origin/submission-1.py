class coord:
    def __init__(self, points):
        self.x = points[0]
        self.y = points[1]
        self.coords = points
    def dist(self):
        return (self.x*self.x + self.y*self.y)
    def __lt__(self, other): #since we are maintaining max-heap (popping farthest points)
        return self.dist() > other.dist() #we have to reverse the < function
    def make_list(self):
        return self.coords
    def __repr__(self):
        return f"[{self.x},{self.y}]"


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = [coord(x) for x in points]
        heapq.heapify(coords)
        while len(coords) > k:
            heapq.heappop(coords)
        return [x.make_list() for x in coords]