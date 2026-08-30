class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        left = 0
        right = left + len(s1) - 1 


        while right < len(s2):


            substring = s2 [left : right+1]
            s1_copy = s1.copy()
            s1_copy = s1.sort()
            
            substring = substring.sort()

            s1_copy = "".join.sorted(s1.copy)
            substring = "".join.sorted(substring.copy)

            if s1_copy == substring:
                return True

            right += 1 
            left += 1
        
        return False

        

    
        