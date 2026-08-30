class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            if t == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(y/x)            
            if t == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)        
            if t == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x) 
            else:
                stack.append(t)             


        return stack[-1]