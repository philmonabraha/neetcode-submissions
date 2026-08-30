class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashmap = {}

        for letter in s:

            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1

        original = k
        
        right = 0
        left = 0
        maxlength = 0

        while right < len(s):

            while s[right] != s[left]:
                
                if k > 0:
                    k -= 1
                    s = s[:right] + s[left] + s[right+1:]

                else:

                    k = original
                    left = right
            
            maxlength = max(maxlength, r - l + 1)
            right += 1

        
        return maxlength
            

            

        







