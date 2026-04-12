# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count length of linked list
        count = 1
        curr = head
        while curr.next:
            count += 1
            curr = curr.next

        remove_index = count - n
        if remove_index == 0:
            head = head.next
        elif remove_index == 1:
            head.next = head.next.next
        else:
            curr = head
            remove_index -= 1
            while remove_index != 0:
                curr = curr.next
                remove_index -= 1
            
            curr.next = curr.next.next

        
        return head

        