class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        #TC & SC : O(logn)
        #Getting basic details and type casting
        n_digits = len(digits)
        n_str = str(n)
        n_len = len(n_str)
        res = 0
        
        #calculating possiblities of count for (n-1) n_len
        for i in range(1,n_len):
            res += n_digits ** i
            
        #calculating count for n equal digits
        for i in range(n_len):
            same_digit = False
            for digit in digits:
                if digit < n_str[i]:
                    res += n_digits ** (n_len-i-1)
                elif digit == n_str[i]:
                    same_digit = True
                    
            if(same_digit==False):
                return res
        
        
        return res+1