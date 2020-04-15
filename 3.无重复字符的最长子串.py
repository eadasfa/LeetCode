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
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
