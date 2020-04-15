#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n==0:
            return head
        first,second = head,head
        for i in range(n):
            second = second.next
        # 表示给定的 n 和 链表长度一样
        if second==None:
            return head.next
        while second.next!=None:
            first = first.next
            second = second.next
        first.next = first.next.next if n!=1 else None
        return head
# print(Solution().removeNthFromEnd([1],1))
# @lc code=end

