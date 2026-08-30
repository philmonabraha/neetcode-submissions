class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        currentwindow = set()
        maxlength = 0

        beginning = 0

        for end in range(len(s)):


            while s[end] not in currentwindow:

                currentwindow.remove(s[beginning])
                beginning += 1

            currentwindow.add(s[end])
            maxlength = max (maxlength, end - beginning + 1)
            
        return maxlength



