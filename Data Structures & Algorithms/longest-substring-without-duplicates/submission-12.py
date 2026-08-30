class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        left = 0
        right = 0

        res = 0
        seen = set()

        while left < right:

            curr = 0
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
                curr += 1
            
            res = max(curr, res) 
            seen.remove(s[left])   
            left += 1

        return res

        