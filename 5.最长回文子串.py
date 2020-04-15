#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.longestPalindrome2(s)
    def longestPalindrome1(self, s):
        n = len(s)
        s2 = s[::-1]
        dp = [ [ 0 for __ in range(n+1)] for _ in range(n+1)]
        max_length = 0
        end_index = 0
        for i in range(n):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j]+1 if s[i] == s2[j] else 0
                if dp[i+1][j+1]>max_length:
                    #  i表示s[i-dp[i+1][j+1]+1:i+1]
                    #  j表示s2[j-dp[i+1][j+1]+1,j+1] -> s[n-j-1,n-(j-dp[i+1][j+1]+1)]
                    # 将范围转换为 对应s的范围，左边应该相等
                    if i-dp[i+1][j+1]+1 == n-j-1:
                        max_length = dp[i+1][j+1]
                        end_index = i
        return s[end_index-max_length+1:end_index+1]
        # return s[n-end_index-1:n-(end_index-max_length+1)]
    def longestPalindrome2(self, s):
        size = len(s)
        max_length = 1
        left,right=0,0
        for i in range(size):
            j,current_length = 1,1
            # 中心是一个，回文字符串位奇数
            while i-j>=0 and i+j<size and s[i-j]==s[i+j]:
                j,current_length=j+1,current_length+2
                if current_length>max_length:
                    max_length,left,right = current_length,i-(j-1),i+(j-1)
            # 中心是两个，回文字符串位奇数
            if not (i+1<size and s[i]==s[i+1]):
                continue
            j,current_length = 1,2
            if current_length > max_length:
                    max_length,left,right = current_length,i,i+1
            while i-j>=0 and i+1+j<size and s[i-j]==s[i+1+j]:
                j,current_length=j+1,current_length+2
                if current_length>max_length:
                    max_length,left,right = current_length,i-(j-1),i+j
        return s[left:right+1]
# s = Solution()
# print(s.longestPalindrome("cbbd"))

# @lc code=end

