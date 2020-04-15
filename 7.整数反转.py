#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y,res = abs(x),0
        boundary = (1<<31)-1 if x>0 else 1<<31
        while y!=0:
            res = res*10+y%10
            y=int(y/10)
        print(res,boundary)
        if res>boundary:
            return 0
        return res if x>0 else -res
# @lc code=end