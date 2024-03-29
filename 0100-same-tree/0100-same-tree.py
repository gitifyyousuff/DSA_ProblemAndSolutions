# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #DFS(Depth First Search) approach to be used
        #Set the base case 
        #if both the trees are empty, then it should be true
        if not p and not q:
            return True
        
        #if one of the tree is empty and other not
        #Also value of p and q are not equal 
        #for the above mentioned 2 conditions, it is False
        if not p or not q or p.val!=q.val:
            return False
        
        #Now perform recursive call (DFS)
        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))
           
     
                    
                    
                
                
        