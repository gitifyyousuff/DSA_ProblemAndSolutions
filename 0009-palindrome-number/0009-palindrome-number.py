class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        rev_int = 0
        temp = x

        while temp!=0:
            dig = temp%10
            rev_int = rev_int*10 + dig
            temp = temp//10
        return x == rev_int