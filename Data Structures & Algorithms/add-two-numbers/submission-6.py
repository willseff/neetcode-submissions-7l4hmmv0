# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = currRes = ListNode(val=0)
        remainder = 0

        while l1 and l2:
            digitSum = l1.val + l2.val + remainder
            if digitSum >= 10:
                currRes.next = ListNode(val=digitSum-10)
                remainder = 1
            else:
                currRes.next = ListNode(val=digitSum)
                remainder = 0

            currRes = currRes.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            digitSum =  l1.val + remainder

            if digitSum == 10:
                digitSum = 0
                remainder = 1
            else:
                remainder = 0
            currRes.next = ListNode(val = digitSum)
            currRes = currRes.next
            l1 = l1.next
        
        while l2:
            digitSum =  l2.val + remainder
            if digitSum == 10:
                digitSum = 0
                remainder = 1
            else:
                remainder = 0
            currRes.next = ListNode(val = digitSum)
            currRes = currRes.next
            l2 = l2.next
        
        if remainder == 1:
            currRes.next = ListNode(val=1)

        return res.next





        