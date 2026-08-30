class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:

            stack.append(i)

            if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/':
                
                operation = stack.pop()
                operand1 = stack.pop()
                operand2 = stack.pop()

                if operation == "/":
                    stack.append(operand1 / operand2)
                elif operation == "*":
                    stack.append(operand1 * operand2)
                elif operation == "+":
                    stack.append(operand1 + operand2)
                elif operation == "-":
                    stack.append(operand1 - operand2)
        
        return stack[-1]