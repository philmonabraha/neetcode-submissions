class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0, 1

        dictionary = {}
        dictionary[s[left]] = 1

        res = 0

        while right < len(s):
               
            while k > 0:

                if s[right] in dictionary:
                    dictionary[s[right]] +=1
                else:
                    dictionary[s[right]] = 1

                if s[right] != s[left]:
                    k -= 1
                
                right += 1

            res = max(res, right - left + 1)

            if s[left] <= s[right]:
                k += 1

            left += 1

        return res




        