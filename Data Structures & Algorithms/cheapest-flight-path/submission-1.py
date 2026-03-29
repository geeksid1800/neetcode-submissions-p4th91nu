'''
Dijkstra's doesn't work here because of the # of stops constraint. Say you could get to a node '2'
in 1 step with cost 5, but in 3 steps with cost 4. If your total stops allowed is 4, and from '2'
to dest requires 2 additional stops, then Dijkstra's would tell us that we can't get to dest 
(because 3+2 stops is it's optimal route). However, we CAN get to dest using '2' in 3 steps using
non-optimal route. This is because Dijkstra's is a greedy algo, and here we may need to make non-
greedy choices. Hence, we use Bellman-Ford, which is not greedy.
If the optimal route to a node N is on a route R edges away from src, it will take R iterations of
B-F to optimise distance to N. If there is a shorter, but less optimal route R' to N, N's dist from
src will be cost(R') after R' turns, and will remain so until Rth iteration. This is ideal, as we
may need to take the non-optimal route to a node, based on the number of stops we are allowed.
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        price = [float('inf')]*n
        price[src] = 0

        for iter in range(k+1): #'k' stops + 1 for dest
            temp = list(price) #deep copy
            for frm,to,cost in flights:
                if price[frm] < float('inf') and price[frm] + cost < temp[to]:
                    temp[to] = price[frm] + cost
            price = temp
        
        return price[dst] if price[dst] < float('inf') else -1