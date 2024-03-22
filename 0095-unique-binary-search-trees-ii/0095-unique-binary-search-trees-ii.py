# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #4^n/n(root(n)) TC --> complex to explain
        dp ={}
        def generateHelper(left,right):
            #Basecase
            if left > right:
                return [None]
            
            #caching mechanism
            if (left,right) in dp:
                return dp[(left,right)]
            res = []
            for val in range(left,right+1):
                for leftTree in generateHelper(left,val-1):
                    for rightTree in generateHelper(val+1, right):
                        root = TreeNode(val,leftTree,rightTree)
                        res.append(root)
                        
            dp[(left,right)] = res 
            return res
        return generateHelper(1,n)