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

