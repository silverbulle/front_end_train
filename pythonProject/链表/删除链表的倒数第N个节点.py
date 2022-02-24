# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(next=head)

        slow, fast = dummy_head, dummy_head
        while (n != 0):  # fast先向前走n步
            fast = fast.next
            n -= 1
        while (fast.next != None):
            slow = slow.next
            fast = fast.next
        # fast走到结尾之后，slow的下一个节点为倒数第N个节点
        slow.next = slow.next.next  # 删除
        return dummy_head.next
