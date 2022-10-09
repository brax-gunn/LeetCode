# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        arr = {}
        self.__dfs(root, arr)
        
        for elem in arr:
            if k - elem != elem:
                if k - elem in arr:
                    return True
        
        return False
    
    def __dfs(self, root, arr):
        
        if root is None:
            return
        
        arr[root.val] = True
        
        self.__dfs(root.left, arr)
        self.__dfs(root.right, arr)
        
        return