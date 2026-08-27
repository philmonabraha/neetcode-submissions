class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for i in strs:

            output = output + str(len(i)) + "#" + i  
       
        return output 


    def decode(self, s: str) -> List[str]:

        output = []

        tracker = 0


        start = 1

        while tracker < len(s):

            
            if s[tracker+1] == '#':
                length = int(s[tracker])
                output.append(s[tracker+2: tracker+2+length])
                tracker = tracker+ 2 +length
            elif s[tracker+2] == '#':
                length = int(s[tracker:tracker+2])
                output.append(s[tracker+3: tracker+3+length])
                tracker = tracker+ 3 +length

            elif s[tracker+3] == '#':
                length = int(s[tracker:tracker+3])
                output.append(s[tracker+4: tracker+4+length])
                tracker = tracker+ 4 +length   

        return output
                    




    

        




