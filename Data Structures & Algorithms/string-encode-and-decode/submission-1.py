class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for st in strs:
            length = str(len(st))
            output += length
            output += st

        return output 

    def decode(self, s: str) -> List[str]:

        output = []

        current = 0

        while current < len(s):

            length = int(s[current])

            st = s[current:current+length]

            current += length

            output.append(st)

        return output



