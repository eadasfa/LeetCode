#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        hmap = {'(':')','{':'}','[':']'}
        for ch in s:
            if ch=='(' or ch=='{' or ch =='[':
                list.append(ch)
            else:
                if len(list)==0 or hmap[list.pop()] != ch:
                    return False
        return True if not list else False
# s = Solution()
# print(s.isValid("()"))
# @lc code=end

