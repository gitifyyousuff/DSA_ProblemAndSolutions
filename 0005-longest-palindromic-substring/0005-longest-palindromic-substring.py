class Solution:
    def longestPalindrome(self, s):

        #result as empty string
        result  =""

        #initialize length of the palindromic substring
        res_len = 0

        for i in range(len(s)):
            #checking palindrome or not by having iterative char of string
            #as centre and checking outwards left and right

            #odd length sub-string
            left,right = i,i


            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > res_len:
                    result = s[left:right+1]
                    res_len = right-left +1
                #expanding the left side and right 
                left -= 1
                right += 1

            #even length sub-string
            left,right = i,i+1


            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > res_len:
                    result = s[left:right+1]
                    res_len = right-left +1
                #expanding the left side and right 
                left -= 1
                right += 1

        return result

            