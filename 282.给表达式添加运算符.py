#
# @lc app=leetcode.cn id=282 lang=python
#
# [282] 给表达式添加运算符
#

# @lc code=start
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        list_num = [ ch for ch in num]
        return self.addRegress(0,list_num,target)
    def addRegress(self,index,num,target,prex=''):
        if len(prex)==0 or prex[-1] in '+-*':
            prex = prex+num[index]
        if index == len(num)-1:
            return [prex] if int(num[index]) == target else []
        # + 和 -
        res = self.addRegress(index+1,num,target-int(num[index]),prex+'+') + \
              self.addRegress(index+1,num,target+int(num[index]),prex+'-') 
        muil = int(num[index])*int(num[index+1])
        temp = num[index+1]
        num[index+1] = str(muil)
        res = res + \
            self.addRegress(index+1,num,target,prex+'*'+temp)
        num[index+1] = temp
        return res
s = Solution()
print(s.addOperators("123",5))
# @lc code=end

