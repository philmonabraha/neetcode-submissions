class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:

            stack.append(i)

            if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '*' or stack[-1] == '/':
                
                operation = stack.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()

                if operation == "/":
                    stack.append(int(operand1) / int(operand2))
                elif operation == "*":
                    stack.append(int(operand1) * int(operand2))
                elif operation == "+":
                    stack.append(int(operand1) + int(operand2))
                elif operation == "-":
                    stack.append(int(operand1) - int(operand2))
        
        return int(stack[-1])