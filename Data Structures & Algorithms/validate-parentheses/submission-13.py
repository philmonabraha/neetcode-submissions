class Solution:
    def isValid(self, s: str) -> bool:

        stack1 = deque()

        pointer1 = 0
        pointer2 = len(s) - 1
        
        while (pointer1 <= pointer2):
            
            

            item1 = s[pointer1]
            item2 = stack1.pop()

            stack1.append(s[pointer1]) 

            if item1 == ")" and item2 != "(":
                return False
            elif item1 == "}" and item2 != "{":
                return False
            elif item1 == "]" and item2 != "[":
                return False

            pointer1 += 1

        return True
        