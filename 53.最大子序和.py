#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.method_one(nums)
        return self.divide(nums,0,len(nums)-1)
    def divide(self,nums,i,j):
        if i>j:
            return -(1<<31)
        if i==j:
            return nums[i]
        middle = (i+j)//2
        x1 = self.divide(nums,i,middle-1)
        x2 = self.divide(nums,middle+1,j)
        # 包括 middle
        left_max_sum,temp=0,0
        for k in range(middle-1,i-1,-1):
            temp += nums[k]
            left_max_sum = temp if temp>left_max_sum else left_max_sum
        right_max_sum,temp=0,0
        for k in range(middle+1,j+1):
            temp += nums[k]
            right_max_sum = temp if temp>right_max_sum else right_max_sum
        x3 = left_max_sum+right_max_sum+nums[middle]
        return max(x1,x2,x3)

    def method_one(self,nums):
        max_, pre = nums[0],nums[0]
        for i in range(1,len(nums)):
            pre = nums[i] if nums[i]>=nums[i]+pre else (nums[i]+pre)
            max_ = max(max_,pre)
        return max_
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))          
# @lc code=end

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''