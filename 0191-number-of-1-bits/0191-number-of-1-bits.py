class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #O(32)
        # count  = 0

        # for i in range(32):
        #     if(n>>i)&1:
        #         count += 1

        # return count

        #O(set-bits)
        count = 0
        while(n!=0):
            n =  n & (n-1)
            count += 1
        return count