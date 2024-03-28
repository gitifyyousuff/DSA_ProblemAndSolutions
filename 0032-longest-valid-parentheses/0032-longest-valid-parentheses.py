class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #stack hold -1 value as default because for the i/p like "(())",
        #stack will be empty and top of the stack have no value result to error
        stack = [-1]
        res = 0
        #iterate the string, add index to stack if it see open parenthesis
        #else pop it and calculate the current valid length and update to max 
        #value in res
        #if stack is completly empty for eg for this "))()())", then add the 
        #current indx
        for i in range(len(s)):
            
            if (s[i] == "("):
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    #current indx - stack top
                    res = max(res,(i-stack[-1]))
                    
        return res
