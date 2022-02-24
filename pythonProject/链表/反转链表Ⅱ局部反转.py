class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverseList(head: ListNode):
            pre = None
            cur = head
            while (cur != None):
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        # 第1步:从虚拟头节点走left-1步，来到left节点的前一个节点
        for _ in range(left - 1):
            pre = pre.next

        right_node = pre
        # 第2步：从pre再走right-left+1步，来到right节点
        for _ in range(right - left + 1):
            right_node = right_node.next
        # 第3步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next
        # 注意：切断链接
        pre.next = None
        right_node = None
        # 第4步：反转链表的子区间
        reverseList(left_node)
        # 第5步：接回到原来的链表中
        pre.next = right_node
        left_node.next = curr
        return dummy_node


class Solution1:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
