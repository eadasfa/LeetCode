#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        stack = []
        temp = ''
        for i in range(len(s)):
            ch = s[i]
            if ch == ' ' :
                continue
            else:
                temp = temp+ch
                if i == len(s)-1 or s[i+1]==' ':
                    stack.append(temp)
                    temp = ''
        temp = stack.pop() if stack else ""
        while stack:
            temp = temp+" "+stack.pop()
        return temp
print(Solution().reverseWords("the sky is blue"))
# @lc code=end

