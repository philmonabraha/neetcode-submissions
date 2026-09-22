class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = {}
        for i in t:
            if i not in t_map:
                t_map[i] = 1
            else:
                t_map[i] += 1

        
        left, right = 0, 0

        res = ""

        s_map = {}

        while right < len(s):

            if s[right] not in s_map:
                s_map[s[right]] = 1
            else:
                s_map[s[right]] += 1

            all_items_present = True
            for i in t_map:
                if i not in s_map or t_map[i] > s_map[i]:
                    all_items_present = False
                    break

            while all_items_present:
                
                if res == "" or right - left + 1 < len(res):
                    res = s[left: right+ 1]
                s_map[s[left]] -= 1
                
                for i in t_map:
                    if i not in s_map or t_map[i] > s_map[i]:
                        all_items_present = False
                        break
                left += 1

            right += 1

        return res

        