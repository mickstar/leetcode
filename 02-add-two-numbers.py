# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2
        added_ln = ListNode(current_l1.val + current_l2.val)
        c_added_ln = added_ln
        while True:
            if current_l1 is not None:
                current_l1 = current_l1.next
            if current_l2 is not None:
                current_l2 = current_l2.next
            if current_l1 is None and current_l2 is None:
                break
            if current_l1 is None:
                l1_v = 0
            else:
                l1_v = current_l1.val
            if current_l2 is None:
                l2_v = 0
            else:
                l2_v = current_l2.val
            v = l1_v + l2_v
            if c_added_ln.val >= 10:
                c_added_ln.val -= 10
                v += 1
            c_added_ln.next = ListNode(v)
            c_added_ln = c_added_ln.next
        
        if (c_added_ln.val >= 10):
            c_added_ln.next = ListNode(1)
            c_added_ln.val = c_added_ln.val - 10
            
        return added_ln
            
