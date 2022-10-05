# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        
        if depth == 1:
            tempNode = TreeNode(val)
            tempNode.left = root
            tempNode.right = None
            
            return tempNode
        
        myQueue = deque()
        
        myQueue.append( (root, 1) )
        
        while len(myQueue) > 0:
            
            node, level = myQueue.popleft()
            
            if level == depth-1:
                leftNode = TreeNode(val)
                rightNode = TreeNode(val)
                
                nextLeftNode = node.left if node is not None else None
                nextRightNode = node.right if node is not None else None
                
                if node is not None:
                    node.left = leftNode 
                    node.right = rightNode 
                
                leftNode.left = nextLeftNode
                rightNode.right = nextRightNode
            
            if node is not None:
                myQueue.append( (node.left, level+1) )
                myQueue.append( (node.right, level+1) )
            
        
        return root
        