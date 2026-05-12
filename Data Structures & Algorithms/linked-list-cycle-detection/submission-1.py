# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[]
        curr=head
        while curr.next:
            if curr.val not in l:
                
                l.append(curr.val)
                curr=curr.next
            else:
                return True
        return False
        