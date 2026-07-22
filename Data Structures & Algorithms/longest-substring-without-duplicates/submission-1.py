class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        maxsofar = 0

        seen = set()

        i, j = 0, 0

        while j < len(s):
            
            while s[j] in seen:
                
                seen.remove(s[i])
                i += 1

            if j-i + 1 > maxsofar:
                maxsofar = j-1 + 1 

            seen.add(s[j])
            j += 1

        return maxsofar










             
        