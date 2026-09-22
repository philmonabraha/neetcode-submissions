class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = {}
        for i in t:
            if i not in t_map:
                t_map[i] = 1
            else:
                t_map[i] += 1

        
        left, right = 0, 0
        need = len(t_map)
        have = 0

        res = ""

        s_map = {}

        while right < len(s):

            if s[right] not in s_map:
                s_map[s[right]] = 1
            else:
                s_map[s[right]] += 1

            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
                have += 1

            while need == have:
                
                if res == "" or right - left + 1 < len(res):
                    res = s[left: right+ 1]
                
                s_map[s[left]] -= 1

                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    have -= 1
        
                left += 1

            right += 1

        return res

        