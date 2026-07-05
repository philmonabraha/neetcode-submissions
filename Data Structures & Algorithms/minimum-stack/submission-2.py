class MinStack:

    def __init__(self):

        self.stack = []
        self.minsofar = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minsofar) == 0:
            self.minsofar.append(val)

        elif val < self.minsofar[-1]:
            self.minsofar.append(val)

    def pop(self) -> None:

        lastelemet = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)-2]

        if self.minsofar[-1] == lastelement:
            self.minsofar.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minsofar[-1]
        
