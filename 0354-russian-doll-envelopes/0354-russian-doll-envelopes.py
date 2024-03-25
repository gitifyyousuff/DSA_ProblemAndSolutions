class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #O(n^2)T 
        '''envelopes.sort()
        n = len(envelopes)
        
        dp = [1]*n
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                #width should not be same
                #height condtn to get Longest consecutive subsequenc
                if envelopes[i][0]!= envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    dp[i] = max(dp[i],1+dp[j])
                    
        return max(dp)'''
    
        #O(nlogn)
        envelopes.sort(key= lambda x:(x[0],-x[1]))    
        n = len(envelopes)
        dp = []
        #binary search operation with inbuilt-function
        for w,h in envelopes:
            idx = bisect.bisect_left(dp,h)
            
            if idx < len(dp):
                dp[idx] = h
            else:
                dp.append(h)
                
        return len(dp) 
            
        
        