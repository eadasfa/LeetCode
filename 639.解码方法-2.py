#
# @lc app=leetcode.cn id=639 lang=python
#
# [639] 解码方法 2
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        last_last = 1
        last = 1 if s[0]!='*' else 9
        for i in range(1,len(s)):
            curr_ch ,last_ch = s[i],s[i-1]
            one = 0 if curr_ch=='0' else last * (1 if curr_ch!='*' else 9)
            two = 0
            if last_ch=='1':
                two = last_last * (1 if curr_ch!='*' else 9)
            elif last_ch=='2':
                two = last_last * ((1 if int(curr_ch)<7 else 0) if curr_ch!='*' else 6)
            elif last_ch=='*':
                two = last_last * (15 if curr_ch=='*' else (2 if int(curr_ch)<7 else 1))
            last,last_last = one+two,last
        return last % ((10**9)+7)

s = Solution()
print(s.numDecodings("*********"))
# @lc code=end

