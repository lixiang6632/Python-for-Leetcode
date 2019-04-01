# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = l1
        carry = 0
        while l1 and l2:
            carry += (l1.val + l2.val)
            l1.val = carry % 10
            carry //= 10
            temp = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            temp.next = l2
        while carry:
            if not temp.next:
                temp.next = ListNode(carry)
                return result
            else:
                temp = temp.next
                carry += temp.val
                temp.val = carry % 10
                carry //= 10
        return result