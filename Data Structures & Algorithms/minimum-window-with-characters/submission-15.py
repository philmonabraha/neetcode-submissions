class Solution:
    def minWindow(self, s: str, t: str) -> str:
      
        
        left, right = 0, 0

        target = {}

        for i in t:

            if i in target:
                target[i] += 1
            else:
                target[i] = 1

        have, need = 0, len(target)
        res = [-1,-1]
        reslen = float("infinity")

        window = {}

        while right < len(s):

            c = s[right]
            if c in window:
                window[c] +=1
            else:
                window[c] = 1

            if c in target and target[c] == window[c]:
                have +=1

            while have == need:
                
                if (right - left + 1) < reslen:
                    res = [left, right]
                    reslen = right - left + 1

                window[s[left]] -= 1

                if s[l] in target and target[s[l]] != window[s[l]]:
                    have -= 1
                
                left +=1 
            
            right +=1 

        if reslen == float("infinity"):
            return ""
        
        return s[res[0]:res[1]+1]



            
                
            





        