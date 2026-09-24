class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        index = len(digits) - 1

        while carry != 0:

            if digits[index] < 9:
                digits[index] += 1
                carry = 0
            
            elif index == 0 and digits[index] >= 9:
                digits = [1] + [0]*len(digits)
                carry = 0

            else:
                digits[index] = 0

            index -= 1
        
        return digits

        