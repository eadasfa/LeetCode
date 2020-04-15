#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        last_one,last_two = 1,2
        for k in range(2, n):
            last_one, last_two =last_two, last_one + last_two
        return last_two
        # return self.An(n)
    def An(self,n):
        n = n+1
        sqrt_5 = 5**(1/2)
        return int(( ((1+sqrt_5)/2)**n-((1-sqrt_5)/2)**n ) / sqrt_5)
num = 2
print(Solution().climbStairs(num))
# print(Solution().An(num))

# @lc code=end

