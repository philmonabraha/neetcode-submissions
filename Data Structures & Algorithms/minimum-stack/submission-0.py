class MinStack:

    def __init__(self):

        stack = []
        minsofar = []
        
    def push(self, val: int) -> None:
        stack = append(val)

        if len(minsofar) == 0:
            minsofar.append(val)

        elif val < minsofar[-1]:
            minsofar.append(val)

    def pop(self) -> None:

        lastelemet = stack[-1]
        stack = stack[0:len(stack)-2]

        if minsofar[-1] == lastelement:
            minsofar.pop()

    def top(self) -> int:
        return stack[-1]
        
    def getMin(self) -> int:
        return minsofar[-1]
        
