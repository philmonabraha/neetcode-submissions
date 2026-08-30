class Solution:
    def convert(self, s: str, numRows: int) -> str:

        


        resultarray = ["" for i in range(numRows)]

        currentrow = 0
        direction = 1

        for letter in s:

            

            if currentrow == 0 or currentrow == numRows - 1:
                direction = direction * -1
            
            resultarray[currentrow] += letter

            currentrow += direction

        return "".join(resultarray)


        