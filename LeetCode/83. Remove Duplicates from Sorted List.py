
class Solution:
    def delete_duplicate(self,head):
        # e.g : linkedlist =None(means previous) 1->2->2->3->4
        current = head 

        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head 



