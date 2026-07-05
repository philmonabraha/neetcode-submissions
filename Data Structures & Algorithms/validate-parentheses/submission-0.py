class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        for item in s:

            if item in ['[', '{', "("]:
                stack.append(item)
            else:

                item2 = stack.pop()

                if (item2 == "[" and item != "]") or (item2 == "{" and item != "}") or (item2 == "(" and item != ")"):
                    return False

        return True


        