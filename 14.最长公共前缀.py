#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # 假设最长公共前缀就是第一个，记录长度
        length = len(strs[0])
        # 遍历其他字符串
        for s in strs[1:]:
            # 该字符串和当前最长公共前缀的公共长度
            common_n = 0
            # 当前字符串和最长公共前缀的长度哪个小
            it = length if length<len(s) else len(s)
            for i in range(it):
                # 逐个比较
                if s[i] == strs[0][i]:
                    common_n+=1
                else:
                    break
            # 没有公共前缀
            if common_n==0:
                return ""
            length = common_n
        return strs[0][:length]
# s = Solution()
# print(s.longestCommonPrefix(["dog","racecar","car"]))
# @lc code=end

