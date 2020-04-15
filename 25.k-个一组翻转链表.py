#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        return self.recursion(head,k)
    def recursion(self,first,k):
        stack= []
        temp = first
        #todo 进栈
        while temp!=None and len(stack)<k :
            stack.append(temp)
            temp = temp.next
        #! 如果栈中 node数量不足k 直接返回
        if len(stack)<k:
            return first
        #todo 记录下下一次递归的第一个 node
        next_fist = stack[-1].next
        #todo 出栈
        temp = first = stack.pop()
        while len(stack)!=0:
            temp.next = stack.pop()
            temp = temp.next
        temp.next = self.recursion(next_fist,k)
        return first
        
        
        
        
        
# @lc code=end

'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''