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

            all_items_present = True
            for i in t_maps:
                if i not in t_maps or t_maps[i] < s_map[i]:
                    all_items_present = False

            while all_items_present:

                res = s[left: right+ 1]
                s_map[left] -= 1
                left += 1

            if right not in s_map:
                s_map[right] = 1
            else:
                s_map[right] += 1
            right += 1

        return res

        