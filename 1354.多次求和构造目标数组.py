#
# @lc app=leetcode.cn id=1354 lang=python
#
# [1354] 多次求和构造目标数组
#

# @lc code=start
class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        flag = 0
        while flag != len(target):
        
            max_i = target.index(max(target))
            sum_except_i = sum(target) - target[max_i]
            target[max_i] = target[max_i] - sum_except_i
            multi = target[max_i]//sum_except_i
         
            flag+=1 if target[max_i]==1 else 0
            if target[max_i]<1 :
                return False
        return True

print(Solution().isPossible([1,1,1,2]))
# @lc code=end

