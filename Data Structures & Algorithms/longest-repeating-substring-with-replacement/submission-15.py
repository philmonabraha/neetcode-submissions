class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        left, right = 0, 0
        res = 0
        maxfreq = 0

        while right < len(s):

            items = s[right]
            if items not in freq:
                freq[items] =  1
            else:
                freq[items] += 1
            
            maxfreq = max(maxfreq, freq[items])
    
            while (right - left + 1) - maxfreq > k:              
                freq[s[left]] -= 1
                left += 1

            res = max(right - left+1, res)
            right += 1
            

        return res
            
                
        
        
        
        