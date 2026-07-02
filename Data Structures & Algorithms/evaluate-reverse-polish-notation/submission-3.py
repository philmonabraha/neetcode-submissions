class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []


        for item in tokens:

            if item not in ['+', "-", "/", "*"]:
                stack.append(item)
            else:

                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if item == '+':
                    stack.append(num1+num2)
                elif item == '*':
                    stack.append(num1*num2)
                elif item == '-':
                    stack.append(num2-num1)
                elif item == '/':
                    stack.append(num2/num1)

        return int(stack[-1])


        