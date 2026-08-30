class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashmap = {}
        
        right = 0
        left = 0


        while right < len(s):

            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1


            while (right - left + 1) - max(hashmap.values()) > k:
                
                hashmap[left] -= 1
                left += 1

            

            maxlength = max(maxlength, right - left + 1)
            right += 1

        
        return maxlength
            

            

        







