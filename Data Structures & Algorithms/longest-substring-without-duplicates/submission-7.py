class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        maxlength = 0

        currentlength = 0

        current = set()
        
        left = 0
        right = 0

        length = len(s)

        while right < length:

            current.add(s[right])

            while s[right] in current:

                current.remove(s[left])
                left += 1

            currentlength += 1

            maxlength = max(currentlength, maxlength)

        
        return maxlength

            

        



            

