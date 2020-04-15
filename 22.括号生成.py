#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.recursion(0,0,n,"",0)

    def recursion(self, left_n, right_n, n, prex, left_pair):
        """
        Args:
            left_n (int): 当前已经附加上几个左括号，并且是有效的
            right_n (int): 当前已经附加上几个右括号，并且是有效的
            prex (string): 前缀
            left_pair (int): 表示左括号还没匹配的个数
        Returns:
            [type]: 结果集
        """
        #todo 右括号已经添加完成，直接返回
        if right_n == n:
            return [prex]
        #! 能到达这说明之前的prex都是有效的，如果左括号没加够，再加一个一定没问题
        res = self.recursion(left_n+1, right_n, n, prex+'(',left_pair+1) if left_n<n else []
        #! 若果左括号还剩余没有被匹配的，这时加一个右括号没问题
        if left_pair>0 :
            res += self.recursion(left_n, right_n+1, n, prex+')',left_pair-1)
        return res

    # def isVaild(self, s):
    #     # ? 时间复杂度为 O(n)
    #     stack=[]
    #     for ch in s:
    #         if ch == '(':
    #             stack.append('(')
    #         elif len(stack) == 0:
    #             return False
    #         else:
    #             stack.pop()
    #     return True
# @lc code=end
'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''
