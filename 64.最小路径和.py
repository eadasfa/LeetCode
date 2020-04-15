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

'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

'''