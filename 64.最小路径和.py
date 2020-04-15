#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        dp = [grid[0][0]]
        for k in range(1,n):
            dp.append(dp[-1]+grid[0][k])
        INFINITE = 1<<31-1
        for i in range(1,m):
            for j in range(n):
                up = dp[j]
                left = dp[j-1] if j-1>=0 else INFINITE
                dp[j] = min(up,left)+grid[i][j]
        return dp[-1]

nums = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution().minPathSum(nums))
# @lc code=end

