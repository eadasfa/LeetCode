#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        right = 0
        for ch in s[::-1]:
            now = hmap[ch]
            res = res-now if now < right else res+now
            right = now
        return res

# @lc code=end

