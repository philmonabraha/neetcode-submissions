class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while True:

            res = 0
            for i in str(n):
                res += int(i) * int(i)

            if res == 1:
                return True
            if res in seen:
                return False
            seen.add(res)
            n = res

        
        