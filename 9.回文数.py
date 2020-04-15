#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        y,res = x,0
        while y!=0:
            res = res*10+ y%10
            y = int(y/10)
        return True if res == x else False
        
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        y,res = x,0
        while y!=0:
            res = res*10+ y%10
            y = int(y/10)
        return True if res == x else False
# @lc code=end

