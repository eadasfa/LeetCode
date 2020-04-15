#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        # 长度不为3时，直接返回
        if length<3:
            return []
        # 快排，从小到大
        self.sortNums(nums,0,len(nums)-1)
        # nums.sort()
        result = []
        # print(nums)
        # 确认第一个数
        for i in range(length-2):
            # 排除重复的，如果nums[i]==nums[i-1]，则第一个数为nums[i]已经算过了
            if i!=0 and nums[i]==nums[i-1]:
                continue
            # nums[i]+nums[i+1]已经大于0了，再加一个肯定大于0
            if nums[i]+nums[i+1]>0:
                return result
            # 数组剩余的，左右两个指针
            left,right = i+1,length-1
            # 左右指针不重合
            while left<right:
                # 相加为0
                if nums[i] + nums[left] + nums[right] == 0 :
                    left,right = left+1,right-1
                    # 判断是否是和上一个加入结果集中的解相同，如果相同，则继续循环
                    if len(result)!=0 and result[-1][0]==nums[i] and result[-1][1]==nums[left-1]:
                        continue
                    # 如果不相同直接加入结果集
                    result.append([nums[i],nums[left-1],nums[right+1]])
                # 如果加起来大于0，只需要right指针向左移动
                elif nums[i] + nums[left] + nums[right]>0:
                    right-=1
                # 如果加起来小于0，只需要left指针向右移动
                else:
                    left+=1
        return result
    def sortNums(self,nums,low,high):
        if low>=high:
            return 
        index = self.partion(nums,low,high)
        self.sortNums(nums,low,index-1)
        self.sortNums(nums,index+1,high)
        # pass
    def partion(self,nums,low,high):
        v = nums[low]
        i,j=low,high
        while i<j:
            while j>i and nums[j]>=v:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
            while j>i and nums[i]<=v:
                i+=1
            nums[i],nums[j] = nums[j],nums[i]
        return i


# print(Solution().threeSum([0,0,0,0,0]))
# @lc code=end

'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''