class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0, 0
        dictionary = {}
        res = 0
        maxfreq = 0

        while right < len(s):

            if s[right] in dictionary:
                dictionary[s[right]] +=1
            else:
                dictionary[s[right]] = 1

            maxfreq = max(maxfreq, dictionary[s[right]])
               
            while right - left + 1 - maxfreq > k:

                dictionary[s[left]] -=1
                left += 1     

            res = max(res, right - left + 1)
            right += 1


        return res




        