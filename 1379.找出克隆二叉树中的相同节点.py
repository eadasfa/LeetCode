#
# @lc app=leetcode.cn id=1379 lang=python
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def porder(original,cloned):
            if original==None:
                return None
            if original==target:
                return cloned
            left = porder(original.left,cloned.left)
            if left:
                return left
            return porder(original.right,cloned.right)
        return porder(original,cloned)
# @lc code=end

