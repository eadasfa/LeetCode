#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        '''分治
        131/131 cases passed (68 ms)
        Your runtime beats 87.6 % of python submissions
        Your memory usage beats 65.79 % of python submissions (18.5 MB)
        '''
        # return divide(0,len(lists)-1)
        '''直接求解
        131/131 cases passed (6952 ms)
        Your runtime beats 5.02 % of python submissions
        Your memory usage beats 65.79 % of python submissions (18.4 MB)
        '''
        return self.directSolve(lists)

    def directSolve(self,lists):
        if not lists:
            return None
        temp = lists[0]
        for ll in lists[1:]:
            temp = self.mergeTwoLists(temp,ll)
        return temp
    def divide(self,i,j):
        if i>=j:
            return None if not lists else lists[i]
        if i+1==j:
            return self.mergeTwoLists(lists[i],lists[j])
        middle = (i+j)//2
        left = self.divide(i,middle)
        right = self.divide(middle+1,j)
        return self.mergeTwoLists(left,right)
    def mergeTwoLists(self, l1, l2):
        """`
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = ListNode(0)
        temp = head
        while l1!=None and l2!=None:
            if l1.val<l2.val:   
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l2==None else l2
        return head.next

# from ListNode import ListNode
# head = ListNode.geneList([1,2,3,4])
# print(ListNode.toList(head))
# @lc code=end

'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''