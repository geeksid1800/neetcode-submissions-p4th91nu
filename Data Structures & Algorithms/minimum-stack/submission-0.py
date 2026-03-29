class MinStack:
    #maintain a min-prefix stack, where a new element is added to the stack
    #only if it smaller than the current top of the stack. That way, it is
    #always increasing. When you pop an element from stack,
    def __init__(self):
        self.stk = [] #just a regular stack for tracking element addition removal etc
        self.minStk = [] #keeps track of minimum element

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minStk) == 0 or val <= self.minStk[-1]:
            self.minStk.append(val) #new min element found

    def pop(self) -> None:
        top = self.stk.pop()
        if self.minStk[-1] == top:
            self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
