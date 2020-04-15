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
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''

