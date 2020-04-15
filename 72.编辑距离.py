#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m==0 or n==0:
            return abs(m-n)
        dp = [ [ 0 for __ in range(n)] for _ in range(m)]
        for k in range(n):
            if word1[0]==word2[k]:
                dp[0][k] = k
            else:
                dp[0][k] = dp[0][k-1]+1 if k-1>=0 else 1
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    if word1[i] == word2[j]:
                        dp[i][j] = i
                    else:
                        dp[i][j] = dp[i-1][j] + 1
                    continue
                # j>=1
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    add = dp[i][j-1] # 增加
                    replace = dp[i-1][j-1] #替换
                    delete = dp[i-1][j] # 删除 
                    dp[i][j] = min(add,replace,delete)+1
        ans = dp[-1][-1]
        return ans
print(Solution().minDistance("horse","ros"))
# @lc code=end

