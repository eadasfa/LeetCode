#
# @lc app=leetcode.cn id=30 lang=python
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_length = len(words[0])
        sub_length = word_length * len(words)
        
        
    def KMP(self,s,p):
        next_ = self.getNext(s)   
        i,j = 0,0
        while i<len(s) and j < len(p):
            if j==-1 or s[i]==p[j]:
                i,j = i+1,j+1
            else:
                j = next_[j]
        if j>=len(p):
            return i-len(p)
        return -1

    def getNext(self,s):
        next_k = [ -1 for _ in range(len(s))]
        i,k = 0,-1
        while i<len(s)-1:
            if k==-1 or s[k] == s[i]:
                k,i=k+1,i+1
                next_k[i] = k
            else :
                k = next_k[k]
        return next_k
# @lc code=end

