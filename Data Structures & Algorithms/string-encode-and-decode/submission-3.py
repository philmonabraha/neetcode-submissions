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
            x = int(index)
            word = s[tracker+1, x]

            tracker = tracker + x 


        return output


    

        




