class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for i in strs:

            output = output + str(len(i)) + i  
       
        return output 


    def decode(self, s: str) -> List[str]:

        output = []

        tracker = 0

        while tracker <= len(s):

            index = s[tracker]
            
            start = tracker+1
            word = s[start:int(index)]

            tracker = tracker + int(index)


        return output


    

        




