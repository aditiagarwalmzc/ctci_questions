# Attempted on Leetcode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Solution 1
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash = {}
        while headA:
            hash[headA] = 1
            headA = headA.next
        
        while headB:
            if headB in hash:
                return headB
            headB = headB.next
        return None

# Solution 2

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tempA, tempB = headA, headB
        lengthA, lengthB = 0, 0
        while tempA:
            lengthA += 1
            tempA = tempA.next
        while tempB:
            lengthB += 1
            tempB = tempB.next
        
        tempA, tempB = headA, headB
        if lengthA > lengthB:
            for _ in range(lengthA - lengthB):
                tempA = tempA.next
        elif lengthB > lengthA:    
            for _ in range(lengthB - lengthA):
                tempB = tempB.next     
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next
            
        return tempA

#Solution 3 -> Neetcode