class Solution:
    def isValid(self, s: str) -> bool:

        stack1 = deque()
        stack2 = deque()

        pointer1 = 0
        pointer2 = len(s) - 1
        
        while (pointer1 <= pointer2):
            stack1.append( s[pointer1] ) 
            pointer1 += 1

            item1 = s[pointer1]
            item2 = stack1.pop()

            if item1 == ")" and item2 != "(":
                return False
            elif item1 == "}" and item2 != "{":
                return False
            elif item1 == "]" and item2 != "[":
                return False

        return True
        