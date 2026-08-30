class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = s.sort()

        t = t.sort()

        return s == t

        