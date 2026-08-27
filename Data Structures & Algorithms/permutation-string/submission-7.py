class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        left = 0
        right = left + len(s1) - 1 


        while right < len(s2):


            substring = s2 [left : right+1]
            s1_copy = s1
            s1_copy = sorted(s1)

            substring = sorted(substring)

            s1_copy = "".join(s1_copy)
            substring = "".join(substring)

            if s1_copy == substring:
                return True

            right += 1 
            left += 1
        
        return False

        

    
        