class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        freq1 = {}
        for s in s1:
            if s not in freq1:
                freq1[s] = 1
            else:
                freq1[s] += 1

        left, right = 0, len(s1)-1

        freq2 = {}
        for i in range(right):
            if s2[i] not in freq2:
                freq2[s2[i]] = 1
            else:
                freq2[s2[i]] += 1
                    
        if freq1 == freq2:
            return True
        while right < len(s2):

            freq2[s2[left]] -= 1
            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            
            if s2[right] in freq2:
                freq2[s2[right]] +=1
            else:
                freq2[s2[right]] = 1

            if freq1 == freq2:
                return True
            
            left += 1
            right += 1
        
        return False




        