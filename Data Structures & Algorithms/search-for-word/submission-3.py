'''
(i,j) - coordinates of current location
ix - index of letter in 'word' we are currently looking for.
Maintain the list of all used coordinates in your current search.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        n = len(word)

        def grid_search(i,j,ix, used):
            # print(f"Looking at {i=},{j=}")
            if ix == n:
                return True
            if i<0 or j<0 or i==r or j==c or (i,j) in used:
                return False
            if word[ix] != board[i][j]:
                return False
            # print(f"found {word[ix]} at {i},{j}")
            used.add((i,j))
            found = grid_search(i+1,j,ix+1,used) or grid_search(i,j+1,ix+1,used) or grid_search(i-1,j,ix+1,used) or grid_search(i,j-1,ix+1,used)
            used.remove((i,j))
            return found

        
        for i in range(r):
            for j in range(c):
                used = set()
                if grid_search(i,j,0, used):
                    return True
    
        return False