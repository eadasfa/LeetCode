#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hmap = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        mlp = 1
        res = ''
        while num!=0:
            t = num % 10
            temp = ""
            if t==4 or t==9:
                temp = hmap[mlp] + hmap[(t+1)*mlp]
            else :
                temp = ""  if t<5 else hmap[5*mlp]
                for i in range(t%5):
                    temp = temp + hmap[mlp]
            res = temp + res
            num = num//10
            mlp*=10
        return res

print(Solution().intToRoman(1994))
# @lc code=end

