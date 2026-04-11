# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = None
        
        if (curr1 and curr2) and (curr1.val < curr2.val):
            head = curr1
            curr1 = curr1.next
        elif (curr1 and curr2):
            head = curr2
            curr2 = curr2.next
        elif curr1:
            head = curr1
            curr1 = curr1.next
        elif curr2:
            head = curr2
            curr2 = curr2.next

        if head:
            merged = head
        else: 
            return None

        while curr1 or curr2:
            if (curr1 and curr2) and (curr1.val > curr2.val):
                merged.next = curr2
                curr2 = curr2.next
            elif (curr1 and curr2):
                merged.next = curr1
                curr1 = curr1.next
            
            elif curr1:
                merged.next = curr1
                curr1 = curr1.next
            
            elif curr2:
                merged.next = curr2
                curr2 = curr2.next

            merged = merged.next
        
        return head
                


        
        