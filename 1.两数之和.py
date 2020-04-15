#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i,num in enumerate(nums):
            another_num = target-num
            if another_num in hmap.keys():
                return [hmap[another_num],i]
            hmap[num] = i
        return None
# @lc code=end

