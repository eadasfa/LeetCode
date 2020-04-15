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

