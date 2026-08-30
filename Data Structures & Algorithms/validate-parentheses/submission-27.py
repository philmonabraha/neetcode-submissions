class Solution:
    def isValid(self, s: str) -> bool:



        stack = []

        for par in s:

            if par == "]":
                if stack and stack.pop() != "[":
                    return False

            elif par == "}":
                if stack and stack.pop() != "{":
                    return False            

            elif par == ")":
                if stack and stack.pop() != "(":
                    return False
            else:
                stack.append(par)
        
        return len(stack) == 0

        