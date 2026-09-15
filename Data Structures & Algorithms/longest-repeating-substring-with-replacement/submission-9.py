class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}

        left, right = 0, 0

        res = 0

        while right < len(s) - 1:

            items = s[right]
            if items not in freq:
                freq[items] =  1
            else:
                freq[items] += 1
    
            while sum(freq.values()) - max(freq.values()) > k:
                
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]

            res = max(right - left, res)
            

        return res
            
                
        
        
        
        