# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import floor

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        midIndex, size = self.__getMidIndex(head)
        
        if size == 1:
            return None
        
        currentIndex = 0
        currentNode = head
        
        while currentIndex < midIndex-1:
            currentIndex += 1
            currentNode = currentNode.next
            
    
        currentNode.next = currentNode.next.next
        return head
    
    def __getMidIndex(self, head):
        size = 0
        
        currentNode = head
        while currentNode is not None:
            size += 1
            currentNode = currentNode.next
        
        return floor(size/2), size