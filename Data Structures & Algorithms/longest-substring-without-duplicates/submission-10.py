class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        maxlength = 0

        currentlength = 0

        current = set()
        
        left = 0
        right = 0

        length = len(s)

        while right < length:


            while s[right] in current:

                current.remove(s[left])
                left += 1

            current.add(s[right])

            maxlength = max(r-l+1, maxlength)

            right += 1

        
        return maxlength

            

        



            

