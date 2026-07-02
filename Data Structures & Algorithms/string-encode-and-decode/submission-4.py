class Solution:
    def encode(self, strs: List[str]) -> str:
        output = []
        for st in strs:
            output.append(str(len(st)) + "#" + st)
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1  # skip '#'
            output.append(s[j:j + length])
            i = j + length

        return output



