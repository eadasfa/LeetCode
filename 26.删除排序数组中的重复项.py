#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index+=1
                nums[index] = nums[i]
        return index+1
# nums = [1,1,2,2,3,4]
# s = Solution()
# print(s.removeDuplicates(nums))
# print(nums)
# @lc code=end

