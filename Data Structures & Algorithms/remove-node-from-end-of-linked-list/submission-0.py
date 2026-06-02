# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        array = []
        temp = current = ListNode()

        while head:
            array.append(head.val)
            head = head.next
        
        array.pop(len(array) - n)

        for num in array:
            current.next = ListNode(num)
            current = current.next
        return temp.next
        