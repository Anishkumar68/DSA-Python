class listNode:
    def __init__(self, val = 0 , next  = None):
        self.val = 0 
        self.next = None

class solution(object):
    def mergesortedlist(self,list1, list2):
        dummy = listNode(0)
        current = dummy 

        while list1 and list2:
            if list1.val <=list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2 
                list2 = list2.next

            current = current.next # current have dummy value so basiclly dummy value updated by reference 
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next 




    