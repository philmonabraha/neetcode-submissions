class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        s_hashmap = dict()

        if len(s) != len(t):
            return False

        for letter in s:

            if letter in s_hashmap:
                s_hashmap[letter] = s_hashmap[letter] + 1
            else:
                s_hashmap[letter] = 1

        for letter in t:

            if letter not in s_hashmap:
                return False

            elif s_hashmap[letter] == 0:
                return False

            else:
                s_hashmap[letter] = s_hashmap[letter] - 1

        return True




        





        return s == t

        