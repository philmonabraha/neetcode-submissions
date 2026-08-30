class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for i in strs:

            output = output + str(len(i)) + i  
       
        return output 


    def decode(self, s: str) -> List[str]:

        output = []

        tracker = 0

        while tracker >= len(str):

            x = int(str[tracker])
            word = str[tracker+1, x]

            tracker = tracker + x 


        return output


    

        




