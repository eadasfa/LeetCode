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

'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''