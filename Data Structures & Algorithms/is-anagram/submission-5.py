class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        left = 0
        right = len(s) - 1

        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        
        for i in s_dict.keys():
            if i not in t_dict:
                return False
            if s_dict[i] != t_dict[i]:
                return False

        return True

                