class Solution:
    def simplifyPath(self, path: str) -> str:
        
        curr = ""
        stk = []
        #so we don't have to handle the last part of input (after last '/') manually
        path += "/" 

        for c in path:
            if c == '/':
                if curr == "" or curr == ".":
                    pass
                elif curr == "..":
                    if len(stk):
                        stk.pop()
                else:
                    stk.append(curr)
                curr = ""
            
            else:
                curr += c
        
        return "/" + "/".join(stk)