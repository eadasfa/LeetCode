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

'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''