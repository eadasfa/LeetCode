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

'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''