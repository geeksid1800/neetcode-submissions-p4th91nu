'''
As with recursive solutions, given a substring of s,s[i:] we will create all palindromic
substrings. This means the first substring of s, upto ith index, has already been broken into
palindromic substrings and placed in 'part'.
The principle is that we will iterate through s[i:] by picking an index j ranging from i+1 to n
and break our current string into [i,j] and [j+1:end]. If s[i:j] is a palindrome, then we have
found a sub-solution, and recurse further down to break the last part.
If s[i:j] isn't a palindrome, then there's no point progressing with that choice of j and we 
don't do anything with this choice of division.  
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def dfs(i, part)-> None:
            #finds all palindromic substrings of s[i:]
            if i == len(s):
                ans.append(part)
                return

            for j in range(i+1,len(s)+1):
                curr = s[i:j]
                if curr == curr[::-1]:
                    dfs(j, part+[curr])

        dfs(0,part)
        return ans 