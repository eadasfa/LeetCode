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

'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''