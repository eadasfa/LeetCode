#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start


class Solution(object):

    def reverse(self, nums, start, end):
        #! 包括end
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 找到最后一个 a[j-1]<a[j]
        j = len(nums)-1
        while j > 0 and nums[j-1] >= nums[j]:
            j -= 1
        # j==0 说明不存在a[j-1]<a[j],即 nums 为逆序，最大，只需将nums反转
        if j == 0:
            self.reverse(nums, 0, len(nums)-1)
            return
        # j是最后一个a[j-1]<a[j]，因此包括j到最后都是逆序的，进行reverse操作
        # 将j及之后的数反转成正序
        self.reverse(nums,j,len(nums)-1)
        # 上一步反转成正序是的数变小了，此时将j-1位的数变大就行
        i = j-1
        while j<len(nums) and nums[i]>=nums[j]:
            j+=1
        nums[i], nums[j] = nums[j], nums[i]
        return nums

# @lc code=end
