"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversed(self,head:ListNode):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def isPalindrome(self, head: ListNode) -> bool:
        fast,mid = head,head
        while(fast and fast.next):
            fast = fast.next.next
            mid = mid.next
            
        fast = head
        mid = self.reversed(mid)
        
        while mid:
            if mid.val != fast.val:
                return False
            mid = mid.next
            fast = fast.next
        return True
        

        
