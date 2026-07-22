class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dictionary = {}

        returnstring = ""

        for i in t:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
            
        dictionary_copy = dictionary


        left, right = 0, len(s) - 1

        while left < right:


            dictionary_copy = dictionary

            while dictionary_copy != {} and left < right and right < len(s):

                if s[right] in dictionary:
                    dictionary[s[right]] = dictionary[s[right]] - 1

                    if dictionary[s[right]] == 0:
                        del dictionary[s[right]]               
                
                right += 1

            if dictionary_copy == {} and len(right-left) > len(returnstring):
                returnstring = s[left:right+1]

            left += 1

        return returnstring










        