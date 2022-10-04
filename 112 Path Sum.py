# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.__isPathSum(root, 0, targetSum)
    
    def __isPathSum(self, root, currSum, targetSum):
        
        if root is None:
            return False
        
        currSum += root.val
        
        if root.left is None and root.right is None:
            return currSum == targetSum
        
        if self.__isPathSum(root.left, currSum, targetSum):
            return True
        
        if self.__isPathSum(root.right, currSum, targetSum):
            return True
        
        return False
        