class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t == "*":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(x*y)
            elif t == "/":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y/x)            
            elif t == "+":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(x+y)        
            elif t == "-":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y-x) 
            else:
                stack.append(t)             


        return int(stack[-1])