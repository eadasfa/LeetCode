#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recursion(head)
        # return self.recursion2(head,2)
        # return self.cycle(head)

    def recursion(self,first):
        '''
        55/55 cases passed (16 ms)
        Your runtime beats 90.67 % of python submissions
        Your memory usage beats 5.26 % of python submissions (12.8 MB)
        '''
        if first == None or first.next==None:
            return first
        second = first.next # 要交换的
        third = second.next # 记录要交换的下一个
        second.next = first # 将第二个几点的next指向first
        first.next = self.recursion(third)
        return second
    def recursion2(self,first,k):
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
        temp.next = self.recursion2(next_fist,k)
        return first

    def cycle(self,head):
        '''
        55/55 cases passed (20 ms)
        Your runtime beats 72.2 % of python submissions
        Your memory usage beats 5.26 % of python submissions (13 MB)
        '''
        if head==None or head.next==None:
            return head
        first = head
        head = ListNode(0)
        last = head
        while first!=None and first.next!=None:
            second = first.next
            third = second.next
            second.next = first
            last.next = second
            first.next = third
            last = first
            first = third
        return head.next
# from ListNode import ListNode
# head = ListNode.geneList([1,2,3,4])
# res = Solution().swapPairs(head)
# print(ListNode.toList(res))
# @lc code=end

