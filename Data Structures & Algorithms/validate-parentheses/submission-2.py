class Solution:
    def isValid(self, s: str) -> bool:


        if len(s) % 2 == 1:
            return False

        stack = []

        for item in s:

            if item in ['[', '{', "("]:
                stack.append(item)
            else:

                if len(stack) == 0:
                    return False

                item2 = stack.pop()

                if (item2 == "[" and item != "]") or (item2 == "{" and item != "}") or (item2 == "(" and item != ")"):
                    return False

        return True


        