class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        
        freq_t = {}

        for i in t:
            if i in freq_t[i]:
                freq_t[i] = 1
            else:
                freq_t[i] += 1

        left, right = 0, len(t)

        freq_s = {}

        for i in range(right):
            if i not in freq_s:
                freq_s[i] = 1
            else:
                freq_s[i] += 1

        res = ""

        def condition(s):
            temp = {}
            for item in s:
                if item not in temp:
                    temp[item] = 1
                else:
                    temp[item] += 1
            
            for key in freq_t.keys():
                if key not in temp or temp[key] < freq_t[key]:
                    return False            
            return True


        while right < len(s):

            while s[left] not in freq_t:
                left += 1
  
            if condition and (right - left) < len(res):
                res = s[left:right]
            
            right += 1

        return res
        
        