# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # counts the length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        print(length)

        start_rev_ind = length // 2

        prev, node = None, head

        i = 0
        while node:
            temp = node.next
            if i >= start_rev_ind:
                node.next = prev
            prev = node
            node = temp
            i += 1
        
        # prev: reversed list
        # head: actual list


        curr = head
        rev_curr = prev
        i = 1
        while i < length:
            print("iteration: " + str(i))
            print(curr.val)
            print(rev_curr.val)
            temp_next = curr.next
            curr.next = rev_curr
            rev_curr = rev_curr.next
            curr.next.next = temp_next
            curr = temp_next
            i += 2
            if i >= length:
                curr.next = None
            




        