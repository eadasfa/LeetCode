#
# @lc app=leetcode.cn id=1290 lang=python
#
# [1290] 二进制链表转整数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res=0
        while head!=None:
            res = (res<<1) + head.val
            # res = res*2 + head.val
            head = head.next
    
        return res

    def getDecimalValue2(self, head):
        num = []
        while head!=None:
            num.append(head.val)
            head = head.next
        res = 0
        for i,n in enumerate(num):
            res += n * (2**(len(num)-1-i)) if n!=0 else 0
        return res

# @lc code=end

