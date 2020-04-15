#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        n1,n2 = len(haystack), len(needle)
        for i in range(n1-n2+1):
            flag = True
            for j in range(n2):
                if needle[j]!=haystack[i+j]:
                    flag = False
                    break
            if flag:
                return i
        return -1

# @lc code=end

