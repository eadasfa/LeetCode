#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    #todo m*n实际上与n*m等价
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [ 1 for _ in range(n)]
        for i in range(1,m):
            for j in range(n):
                dp[j] = dp[j] + ( dp[j-1] if j-1>=0 else 0)
        return dp[-1]
print(Solution().uniquePaths(3,2))
# @lc code=end

