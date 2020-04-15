#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n==0:
            return 0
        temp = [ 1 for _ in range(n)]
        m = temp[0]
        for i in range(1,n):
            if s[i] not in s[i-temp[i-1]:i]:
                temp[i] = temp[i-1] + 1
                m = m if temp[i]< m else temp[i]
            else:
                index = s[i-temp[i-1]:i].index(s[i])
                temp[i] = temp[i-1] - index
        return m

s = Solution()
print(s.lengthOfLongestSubstring(" "))


# @lc code=end

