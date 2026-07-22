class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dictionary = {}

        for i in s1:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        left, right = 0, 0

        dictionary2 = {}

        while right < len(s2):

            while right - left < len(s1):
                
                if s2[right] in dictionary2:
                    dictionary2[s2[right]] += 1
                else:
                    dictionary2[s2[right]] = 1

                if dictionary == dictionary2:
                    return True

                right += 1
           
            

            dictionary2[s2[left]] -= 1           
            if dictionary2[s2[left]] == 0:
                del dictionary2[s2[left]] 
            left += 1     

        return False
            




        

            

        