# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        currentNode = node
        nextNode = node.next
        
        currentNode.val = nextNode.val
        currentNode.next = nextNode.next
        