#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start,end=-1,-1
        nums = '1234567890'
        for i in range(len(str)):
            if start==-1:
                if str[i] =='-' or str[i] == '+' or str[i] in nums:
                    start = i
                elif str[i] != ' ':
                    return 0
                continue
            if str[i] not in nums:
                end = i
                break
        end = len(str) if end==-1 else end
        # 排除只有空格的字符串和只有+-的字符串
        if start==-1 or (end-start==1 and (str[start] in '+-')):
            return 0
        res = int(str[start:end])
        if res > (1<<31)-1:
            return (1<<31)-1
        if res < -(1<<31):
            return -(1<<31)
        return res 
# s = Solution()
# print(s.myAtoi('2147483646'))
# @lc code=end

