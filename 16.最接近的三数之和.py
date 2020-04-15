#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_, sum_ = 1<<31, 0
        for i in range(len(nums)):
            left,right = i+1,len(nums)-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right] - target
                min_,sum_ = (abs(temp),temp+target) if min_ > abs(temp) \
                    else (min_,sum_)
                if temp==0:
                    return sum_
                if temp>0:
                    right-=1
                else:
                    left+=1
        return sum_
# print(Solution().threeSumClosest([-1,2,1,-4],1))
# @lc code=end

