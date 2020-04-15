#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        res = ['' for _ in range(numRows)]
        # 周期
        T = numRows + numRows -2
        for i in range(len(s)):
            t_num = i%T
            temp = t_num if t_num<numRows else numRows-(t_num)%numRows-2
            res[temp] += s[i] 
        return ''.join(res)
# s = Solution()
# print(s.convert("LEETCODEISHIRING",4))
'''
1158/1158 cases passed (56 ms)
Your runtime beats 63.54 % of python submissions
Your memory usage beats 8 % of python submissions (12.7 MB)
'''
# @lc code=end

