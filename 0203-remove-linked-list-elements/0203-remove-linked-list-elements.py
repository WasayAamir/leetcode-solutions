# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head) #this dummy is the kept before the head node
        prev, curr = dummy, head   #two pointers prev right before head so its at dummy and curr is at head 

        while curr:                 # while current is not null or still in the list
            nxt = curr.next         # initalize a variable nxt to make it easier to update current pointer

            if curr.val == val:     #if the current value is the target value we need to remove it
                prev.next = nxt     # we remove it and the prev pointer goes to node after curr
            else:
                prev = curr         #if current is not the value target we move curr to the next node and prev comes to current
            curr = nxt               #update curr pointer to the next node after it regardless
        return dummy.next            # in the end return dummy.next which is the new head