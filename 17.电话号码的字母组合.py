#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        hmap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return self.regress(0,digits,hmap,"")
    def regress(self,index,digits,hmap,prex):
        if index==len(digits):
            return [prex]
        res = []
        for ch in hmap[digits[index]]:
            res += self.regress(index+1,digits,hmap,prex+ch)
        return res
# print(Solution().letterCombinations(""))
# @lc code=end

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
