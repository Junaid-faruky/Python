class Node:
    def __ init__(self, d):
        self.data = d
        self.next = None
        self.prev = None  

class LL:
    def __init__(self):
         self.head = None
    
    def add_node(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            traveller = self.head
            while(traveller.next != None):
                traveller = traveller.next
                traveller.next = new_node
                new_node.prev = traveller  
    
    def traverse(self):
        traveller = self.head
        while(traveller != None):
            print(traveller.data)
            traveller = traveller.next
        
    
    def delete_node(self, val):
        traveller = self.head
        
        while(traveller is not None and traveller.data != val):
            prev = traveller
            traveller = traveller.next
        
        if traveller is None:
            print("Node with value", val)
            return
        
        if traveller.prev:  
            traveller.prev.next = traveller.next
        if traveller.next:  
            traveller.next.prev = traveller.prev
        if traveller == self.head:  
            self.head = traveller.next
        traveller = None

    def delete_at_start(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head:  
                self.head.prev = None

    def add_node_at_start(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head:  
            self.head.prev = new_node
        self.head = new_node


LL1 = LL()
LL1.add_node(3)
LL1.add_node(8)
LL1.add_node(6)
LL1.add_node(1)
LL1.traverse()
LL1.delete_at_start()
LL1.add_node_at_start(5)  
LL1.traverse()
