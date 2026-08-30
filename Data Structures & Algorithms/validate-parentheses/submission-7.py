class Solution:
    def isValid(self, s: str) -> bool:

        stack1 = deque()
        stack2 = deque()

        pointer1 = 0
        pointer2 = len(s) - 1
        
        while (pointer2 - pointer1 >= 1):
            stack1.append( s[pointer1] ) 
            stack2.append( s[pointer2] )

            pointer1 += 1
            pointer2 -= 1
        
        while (len(stack1) != 0 or len(stack2) != 0):

            item1 = stack1.pop()
            item2 = stack2.pop()

            if item1 == "(" and item2 != ")":
                return False
            elif item1 == "{" and item2 != "}":
                return False
            elif item1 == "[" and item2 != "]":
                return False


        return True
        