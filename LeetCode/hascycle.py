class solution:
    def hascycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next #take one step
            fast = fast.next.next # 2steps
            # if fast catch slow return True
            if slow == fast:
                return True
        return False