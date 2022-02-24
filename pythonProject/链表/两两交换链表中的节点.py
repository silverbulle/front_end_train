# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        pre = dummy_head

        # 必须有pre的下一个和下下一个才能交换，否则说明交换已经结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre，cur，post对应最左，中间，最右的节点
            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return dummy_head.next
