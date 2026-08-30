class Solution:

    def encode(self, strs: List[str]) -> str:

        ouput = ""
        for s in strs:
            ouput = output + str(len(s)) + "#" + s
        
        return output

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0

        while i < len(s):
            if s[i] == "#":
                length = s [0:i-1]
                word = s [i: i+length]
                output.append(word)
                s = s[i+length:]        
            i += 1
        
        return output


            

            

            

