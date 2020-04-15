class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    @classmethod
    def geneList(cls,nums):
        if len(nums)==0:
            return None
        head = ListNode(0)
        temp = head
        for i in range(len(nums)):
            temp.next = ListNode(nums[i])
            temp = temp.next
        return head.next
    @classmethod
    def toList(cls,head):
        res = []
        while head!=None:
            res.append(head.val)
            head = head.next
        return res