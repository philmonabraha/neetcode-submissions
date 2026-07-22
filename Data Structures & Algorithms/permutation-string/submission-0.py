class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dictionary = {}

        for i in s1:
            if i in s1:
                dictionary[i] += 1
            else:
                dictionary[i] == 1

        left, right = 0, 0

        dictionary2 = {}

        while right < len(s2):

            while s2[right] in dictionary and right - left < len(s1):
                
                if s2[right] in dictionary2:
                    dictionary2[s2[right]] += 1
                else:
                    dictionary2[s2[right]] = 1

                if dictionary == dictionary2:
                    return True

                right += 1
           
            dictionary[s[left]] -= 1           
            if dictionary[s[left]] == 0:
                del dictionary[s[left]]      

        return False
            




        

            

        