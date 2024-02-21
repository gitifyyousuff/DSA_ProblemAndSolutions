class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        indx = len(digits)-1
        while digits[indx]==9:
            digits[indx] = 0
            indx = indx -1
        if (indx<0):
            digits = [1] + digits
        else:
            digits[indx] = digits[indx] + 1
        
        return digits
        