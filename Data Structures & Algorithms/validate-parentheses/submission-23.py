class Solution:
    def isValid(self, s: str) -> bool:

        stack1 = deque()

        pointer1 = 0
        pointer2 = len(s)
        
        for pointer1 in range(len(s)):
        
            stack1.append(s[pointer1]) 

            item1 = s[pointer1]

            if item1 == ")":
                stack1.pop()
                if len(stack1) == 0 or stack1.pop() != "(":
                    return False
            elif item1 == "}":
                stack1.pop()
                if len(stack1) == 0 or stack1.pop() != "{":
                    return False
            elif item1 == "]":
                stack1.pop()
                if len(stack1) == 0 or stack1.pop() != "[":
                    return False

            pointer1 += 1

        if pointer2 % 2 == 1 or len(stack1) != 0:
            return False
        return True
        