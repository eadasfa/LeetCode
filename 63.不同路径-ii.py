#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [ 0 for _ in range(n)]
        for i in range(n):
            if obstacleGrid[0][i]==1:
                break
            dp[i] = 1
        for i in range(1,m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + ( dp[j-1] if j-1>=0 else 0)
        return dp[-1]
nums = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(Solution().uniquePathsWithObstacles(nums))
# @lc code=end

