class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self,value):
        # we created 2 pointer
        new_node = Node(value)
        self.head = new_node
        self.tail= new_node
        self.len = 1 

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node    
        self.len +=1
           
    def pop(self):
        if self.len == 0:
            return None
        temp = self.head
        pre= self.head

        # 11->5->4->None
        while (temp.next):
            pre = temp
            temp = temp.next
            # when temp = None break
        # then, self.tail value will be pre means -1 so pre =5 
        self.tail = pre 
        self.tail.next = None
        self.len -=1
        if self.len == 0:
            self.head = self.tail = None

    def prepend(self,value):
        new_node = Node(value)
        if self.len == 0:
            self.head = self.tail= new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.len +=1
        return True






        