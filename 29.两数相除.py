#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return None
        flag = 1 if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else -1
        dividend,divisor,res = abs(dividend),abs(divisor), 0
        pre = 0
        for x in str(dividend):
            res *= 10
            sub_dividend = int(x)+pre*10
            while sub_dividend-divisor>=0:
                sub_dividend -= divisor
                res += 1
            pre = sub_dividend
        res = res if flag>0 else -res
        return res if res <= (1<<31)-1 else ((1<<31)-1)
print(Solution().divide(11,-5))
# @lc code=end

